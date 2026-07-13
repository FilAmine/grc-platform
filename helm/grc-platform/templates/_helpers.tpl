{{/*
Chart name, truncated to fit Kubernetes' 63-char label-value limit.
*/}}
{{- define "grc-platform.name" -}}
{{- .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Release-scoped name prefix, so multiple releases of this chart can
coexist in one namespace without colliding.
*/}}
{{- define "grc-platform.fullname" -}}
{{- printf "%s-%s" .Release.Name .Chart.Name | trunc 63 | trimSuffix "-" -}}
{{- end -}}

{{/*
Common labels applied to every resource.
*/}}
{{- define "grc-platform.labels" -}}
app.kubernetes.io/name: {{ include "grc-platform.name" . }}
app.kubernetes.io/instance: {{ .Release.Name }}
app.kubernetes.io/managed-by: {{ .Release.Service }}
helm.sh/chart: {{ printf "%s-%s" .Chart.Name .Chart.Version | replace "+" "_" }}
{{- end -}}
