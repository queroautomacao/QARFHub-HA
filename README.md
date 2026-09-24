<p align="center">
  <img src="logo.png" alt="Quero Automação — QA RF Hub" width="300">
</p>

# QA RF Hub — Home Assistant

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

Integração do **QA RF Hub** com o Home Assistant: cortinas Somfy e cortinas RF aprendidas no Hub.

## Instalação

**HACS:** ⋮ → **Repositórios customizados** → adicione `https://github.com/queroautomacao/QARFHub-HA` (categoria *Integration*) → instale **QA RF Hub** → reinicie o Home Assistant.

**Manual:** copie `custom_components/qarfhub` para `config/custom_components/` e reinicie o Home Assistant.

## Configuração

O Hub aparece sozinho em **Configurações → Dispositivos e serviços**. Se não aparecer, adicione **QA RF Hub** com o IP do Hub.

## Entidades

- **Cortina Somfy**: abrir, fechar e posição (0–100%)
- **Cortina RF**: abrir, parar e fechar; o estado é o do último comando

## Eventos

`qarfhub_event`, nos comandos Somfy: `entity_id`, `event_key`, `name`, `source` (`remote`, `internal`, `group`), `remote_address`, `source_address`, `command` (`Up`, `Down`, `My`, `StepUp`, `StepDown`, `Prog`, `My+Up`, `My+Down`, `Up+Down`, `My+Up+Down`).
