import { zodResolver } from '@hookform/resolvers/zod';
import AddIcon from '@mui/icons-material/Add';
import LibraryBooksIcon from '@mui/icons-material/LibraryBooks';
import SendIcon from '@mui/icons-material/Send';
import {
  Box,
  Button,
  Chip,
  Container,
  Dialog,
  DialogActions,
  DialogContent,
  DialogTitle,
  Divider,
  IconButton,
  List,
  ListItemButton,
  ListItemText,
  Paper,
  Stack,
  TextField,
  Tooltip,
  Typography,
} from '@mui/material';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useEffect, useRef, useState } from 'react';
import { useForm } from 'react-hook-form';
import { z } from 'zod';
import {
  addKnowledgeBaseDocument,
  createChatSession,
  createPromptTemplate,
  getChatMessages,
  getChatSessions,
  getPromptTemplates,
  sendChatMessage,
} from '../api/ai';

const templateSchema = z.object({
  name: z.string().min(2, 'At least 2 characters'),
  description: z.string().optional(),
  template_text: z.string().min(1, 'Required'),
});
type TemplateFormValues = z.infer<typeof templateSchema>;

const kbSchema = z.object({
  title: z.string().min(2, 'At least 2 characters'),
  content: z.string().min(1, 'Required'),
});
type KbFormValues = z.infer<typeof kbSchema>;

export function AiChatPage() {
  const queryClient = useQueryClient();
  const [selectedSessionId, setSelectedSessionId] = useState<string | null>(null);
  const [draft, setDraft] = useState('');
  const [templateDialogOpen, setTemplateDialogOpen] = useState(false);
  const [kbDialogOpen, setKbDialogOpen] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement | null>(null);

  const sessions = useQuery({ queryKey: ['chat-sessions'], queryFn: getChatSessions });
  const templates = useQuery({ queryKey: ['prompt-templates'], queryFn: getPromptTemplates });
  const messages = useQuery({
    queryKey: ['chat-sessions', selectedSessionId, 'messages'],
    queryFn: () => getChatMessages(selectedSessionId!),
    enabled: Boolean(selectedSessionId),
  });

  useEffect(() => {
    if (!selectedSessionId && sessions.data?.length) {
      setSelectedSessionId(sessions.data[0].id);
    }
  }, [sessions.data, selectedSessionId]);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
  }, [messages.data]);

  const createSessionMutation = useMutation({
    mutationFn: () => createChatSession(),
    onSuccess: async (session) => {
      await queryClient.invalidateQueries({ queryKey: ['chat-sessions'] });
      setSelectedSessionId(session.id);
    },
  });

  const sendMutation = useMutation({
    mutationFn: (content: string) => sendChatMessage(selectedSessionId!, { content }),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['chat-sessions', selectedSessionId, 'messages'] });
      setDraft('');
    },
  });

  const templateForm = useForm<TemplateFormValues>({ resolver: zodResolver(templateSchema) });
  const createTemplateMutation = useMutation({
    mutationFn: (values: TemplateFormValues) => createPromptTemplate(values),
    onSuccess: async () => {
      await queryClient.invalidateQueries({ queryKey: ['prompt-templates'] });
      setTemplateDialogOpen(false);
      templateForm.reset();
    },
  });

  const kbForm = useForm<KbFormValues>({ resolver: zodResolver(kbSchema) });
  const addKbMutation = useMutation({
    mutationFn: (values: KbFormValues) => addKnowledgeBaseDocument(values),
    onSuccess: () => {
      setKbDialogOpen(false);
      kbForm.reset();
    },
  });

  const handleSend = () => {
    const content = draft.trim();
    if (!content || !selectedSessionId) return;
    sendMutation.mutate(content);
  };

  return (
    <Container maxWidth="xl" sx={{ py: 4 }}>
      <Stack direction="row" alignItems="center" justifyContent="space-between" sx={{ mb: 3 }}>
        <Box>
          <Typography variant="h4">AI Assistant</Typography>
          <Typography color="text.secondary">Ask questions grounded in your organization's knowledge base.</Typography>
        </Box>
        <Tooltip title="Add a document to the knowledge base the assistant draws context from">
          <Button variant="outlined" startIcon={<AddIcon />} onClick={() => setKbDialogOpen(true)}>
            Add context document
          </Button>
        </Tooltip>
      </Stack>

      <Stack direction="row" spacing={2} sx={{ height: 620 }}>
        <Paper elevation={0} sx={{ width: 280, border: '1px solid', borderColor: 'divider', display: 'flex', flexDirection: 'column' }}>
          <Box sx={{ p: 1.5 }}>
            <Button
              fullWidth
              variant="contained"
              startIcon={<AddIcon />}
              onClick={() => createSessionMutation.mutate()}
              disabled={createSessionMutation.isPending}
            >
              New chat
            </Button>
          </Box>
          <Divider />
          <List sx={{ overflowY: 'auto', flexGrow: 1 }}>
            {(sessions.data ?? []).map((session) => (
              <ListItemButton
                key={session.id}
                selected={session.id === selectedSessionId}
                onClick={() => setSelectedSessionId(session.id)}
              >
                <ListItemText
                  primary={session.title}
                  secondary={new Date(session.updated_at).toLocaleDateString()}
                  primaryTypographyProps={{ noWrap: true }}
                />
              </ListItemButton>
            ))}
            {!sessions.data?.length && (
              <Typography variant="body2" color="text.secondary" sx={{ p: 2 }}>
                No chats yet.
              </Typography>
            )}
          </List>
        </Paper>

        <Paper
          elevation={0}
          sx={{ flexGrow: 1, border: '1px solid', borderColor: 'divider', display: 'flex', flexDirection: 'column' }}
        >
          {!selectedSessionId && (
            <Box sx={{ m: 'auto', textAlign: 'center' }}>
              <Typography color="text.secondary">Start a new chat to talk to the assistant.</Typography>
            </Box>
          )}

          {selectedSessionId && (
            <>
              <Box sx={{ flexGrow: 1, overflowY: 'auto', p: 2 }}>
                <Stack spacing={1.5}>
                  {(messages.data ?? []).map((message) => (
                    <Box
                      key={message.id}
                      sx={{
                        alignSelf: message.role === 'user' ? 'flex-end' : 'flex-start',
                        maxWidth: '75%',
                      }}
                    >
                      <Paper
                        elevation={0}
                        sx={{
                          p: 1.5,
                          bgcolor: message.role === 'user' ? 'primary.main' : 'action.hover',
                          color: message.role === 'user' ? 'primary.contrastText' : 'text.primary',
                          borderRadius: 2,
                        }}
                      >
                        <Typography variant="body2" sx={{ whiteSpace: 'pre-wrap' }}>
                          {message.content}
                        </Typography>
                      </Paper>
                    </Box>
                  ))}
                  {!messages.data?.length && (
                    <Typography variant="body2" color="text.secondary">
                      No messages yet — say hello.
                    </Typography>
                  )}
                  <div ref={messagesEndRef} />
                </Stack>
              </Box>

              <Divider />

              <Box sx={{ p: 1.5 }}>
                <Stack direction="row" spacing={0.5} sx={{ mb: 1, flexWrap: 'wrap' }} useFlexGap alignItems="center">
                  <LibraryBooksIcon fontSize="small" color="action" />
                  {(templates.data ?? []).map((template) => (
                    <Chip
                      key={template.id}
                      size="small"
                      label={template.name}
                      variant="outlined"
                      onClick={() => setDraft(template.template_text)}
                    />
                  ))}
                  <Chip
                    size="small"
                    icon={<AddIcon fontSize="small" />}
                    label="New prompt"
                    onClick={() => setTemplateDialogOpen(true)}
                  />
                </Stack>
                <Stack direction="row" spacing={1}>
                  <TextField
                    fullWidth
                    multiline
                    maxRows={4}
                    placeholder="Ask the assistant..."
                    value={draft}
                    onChange={(event) => setDraft(event.target.value)}
                    onKeyDown={(event) => {
                      if (event.key === 'Enter' && !event.shiftKey) {
                        event.preventDefault();
                        handleSend();
                      }
                    }}
                  />
                  <Button
                    variant="contained"
                    endIcon={<SendIcon />}
                    onClick={handleSend}
                    disabled={sendMutation.isPending || !draft.trim()}
                  >
                    Send
                  </Button>
                </Stack>
              </Box>
            </>
          )}
        </Paper>
      </Stack>

      <Dialog open={templateDialogOpen} onClose={() => setTemplateDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={templateForm.handleSubmit((v) => createTemplateMutation.mutate(v))} noValidate>
          <DialogTitle>New prompt template</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <TextField
                label="Name"
                error={Boolean(templateForm.formState.errors.name)}
                helperText={templateForm.formState.errors.name?.message}
                {...templateForm.register('name')}
              />
              <TextField label="Description (optional)" {...templateForm.register('description')} />
              <TextField
                label="Prompt text"
                multiline
                minRows={3}
                error={Boolean(templateForm.formState.errors.template_text)}
                helperText={templateForm.formState.errors.template_text?.message}
                {...templateForm.register('template_text')}
              />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setTemplateDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={templateForm.formState.isSubmitting}>
              Create
            </Button>
          </DialogActions>
        </Box>
      </Dialog>

      <Dialog open={kbDialogOpen} onClose={() => setKbDialogOpen(false)} fullWidth maxWidth="sm">
        <Box component="form" onSubmit={kbForm.handleSubmit((v) => addKbMutation.mutate(v))} noValidate>
          <DialogTitle>Add context document</DialogTitle>
          <DialogContent>
            <Stack spacing={2} sx={{ mt: 1 }}>
              <Typography variant="body2" color="text.secondary">
                The assistant searches this text for relevant context when answering questions.
              </Typography>
              <TextField
                label="Title"
                error={Boolean(kbForm.formState.errors.title)}
                helperText={kbForm.formState.errors.title?.message}
                {...kbForm.register('title')}
              />
              <TextField
                label="Content"
                multiline
                minRows={4}
                error={Boolean(kbForm.formState.errors.content)}
                helperText={kbForm.formState.errors.content?.message}
                {...kbForm.register('content')}
              />
            </Stack>
          </DialogContent>
          <DialogActions>
            <Button onClick={() => setKbDialogOpen(false)}>Cancel</Button>
            <Button type="submit" variant="contained" disabled={kbForm.formState.isSubmitting}>
              Add
            </Button>
          </DialogActions>
        </Box>
      </Dialog>
    </Container>
  );
}
