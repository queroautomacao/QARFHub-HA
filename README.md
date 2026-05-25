<p align="center">
  <img src="logo.png" alt="Quero Automação — QA RF Hub" width="300">
</p>

# QA RF Hub — Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

Integração oficial do **QA RF Hub** para Home Assistant — controle de cortinas Somfy RTS e cortinas RF (433 MHz, protocolos abertos) a partir do mesmo gateway ESP32.

Esta integração é um fork da ESPSomfy-RTS-HA que adiciona suporte aos **dispositivos RF de protocolo aberto** (PT2262, EV1527, HT6P20B, OOK genérico, Dooya) aprendidos pelo firmware QA RF Hub.

## Recursos

- Até 8 cortinas Somfy RTS ou RF de código fixo aprendidos de controles físicos
- Protocolos: **PT2262**, **EV1527**, **HT6P20B**, **OOK genérico (Period-OOK)**, **Dooya**
- Cada dispositivo tem até 3 códigos (Abrir / Parar / Fechar) → exposto como entity `cover` no HA
- Atualizações de estado via WebSocket (evento `rfState`)
- UI otimista: HA reflete o comando imediatamente enquanto aguarda confirmação do firmware

## Instalação

### Via HACS (recomendado)
1. HACS → menu de 3 pontos → **Repositórios customizados**
2. Adicione `https://github.com/queroautomacao/QARFHub-HA` (categoria: *Integration*)
3. Instale **QA RF Hub**
4. Reinicie o Home Assistant

### Manual
Copie `custom_components/qarfhub` para `config/custom_components/` e reinicie o HA.

## Configuração

Após instalação, o QA RF Hub é auto-detectado via SSDP / Zeroconf na rede local. Vá em **Configurações → Dispositivos & Serviços** e adicione a integração.

Se a auto-detecção falhar, adicione manualmente fornecendo o IP da placa.

## Atualização de firmware

Atualizações são gerenciadas pelo entity `update` que aparece no HA. O HA notifica quando há nova versão publicada no feed de releases do GitHub.

## Funcionalidade

### Cortinas Somfy RTS
Abrir, fechar, posicionar (0–100%). A integração rastreia a posição independentemente da fonte do comando (HA, WebUI da placa, controle Telis). Adicione aos dashboards e crie automações como em qualquer entity `cover`.

### Dispositivos RF abertos
Cada dispositivo RF aprendido aparece como um `cover` com **Abrir / Parar / Fechar**. Como o protocolo é unidirecional (sem feedback do motor), o estado é **lógico** — reflete o último comando enviado, não a posição real do motor.

Dispositivos com 2 códigos (apenas Abrir + Fechar, sem Parar) também são suportados — o botão Parar simplesmente não tem efeito.

## Eventos

A integração emite eventos no event bus do HA para todos os comandos Somfy RTS, com tipo `qarfhub_event`. Payload:

* `entity_id`, `event_key`, `name`
* `source`: `remote` / `internal` / `group`
* `remote_address`, `source_address`
* `command`: `Up` / `Down` / `My` / `StepUp` / `StepDown` / `Prog` / `My+Up` / `My+Down` / `Up+Down` / `My+Up+Down`

Dispositivos RF não emitem eventos (não há rolling code ou identificação de remote).
