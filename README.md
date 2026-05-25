# QA RF Hub — Home Assistant Integration

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-41BDF5.svg?style=for-the-badge)](https://github.com/hacs/integration)

This integration is a fork of [rstrouse/ESPSomfy-RTS-HA](https://github.com/rstrouse/ESPSomfy-RTS-HA) that adds support for the **QA RF Hub** firmware — an extension of ESPSomfy RTS that adds **open-protocol RF device** control (PT2262, EV1527, HT6P20B, Period-OOK, Dooya) alongside the original Somfy RTS shades.

Use this integration if your ESP32 + CC1101 device runs the **QA RF Hub** firmware. It is fully backwards-compatible with the original ESPSomfy RTS firmware (RF device features simply won't appear if the firmware does not expose them).

## Features

### Somfy RTS shades (original ESPSomfy RTS functionality)
- Up to 32 Somfy RTS shades + 16 groups
- Two-way: position feedback even when controlled by a physical Telis remote
- Full set of services (positioning, tilting, sun/wind sensor flags, raw commands)
- Firmware updates via the HA `update` entity

### QA RF Hub — Open-protocol RF devices (new)
- Up to 16 fixed-code RF devices learned from physical remotes
- Supported protocols: **PT2262**, **EV1527**, **HT6P20B**, **Period-OOK** (generic OOK), **Dooya**
- Each device has up to 3 codes (OPEN / STOP / CLOSE) → exposed as a HA `cover` entity
- State updates via WebSocket (`rfState` event)
- Optimistic UI: HA shows the command immediately while waiting for firmware confirmation

## Requirements

ESP32 board (DevKitC-1 N16R8 recommended) + CC1101 433 MHz transceiver running the **QA RF Hub** firmware. The original ESPSomfy RTS firmware also works, but only the Somfy RTS features will be available.

## Installation

### HACS (recommended)
1. Open HACS → 3-dot menu → **Custom repositories**
2. Add `https://github.com/qa-automacao/QARFHub-HA` (category: Integration)
3. Install **QA RF Hub (ESPSomfy RTS + Open RF)**
4. Restart Home Assistant

### Manual
Copy `custom_components/espsomfy_rts` into `config/custom_components/` and restart HA.

## Setup

After installation, the QA RF Hub is auto-discovered via SSDP / Zeroconf on your local network. Go to **Settings → Devices & Services** and add the integration.

If auto-discovery fails, add manually by providing the device IP.

## Updates

Firmware updates are managed via the included `update` entity. Home Assistant will notify you when a new firmware version is published in the GitHub release feed.

## Functionality

### Somfy RTS shades
Open, close, set position (0-100%), tilt control. The integration tracks the shade position regardless of whether the command came from HA, the web UI, or a Telis remote. Add shades to dashboards and create automations as with any cover entity.

### RF devices (open protocol)
Each learned RF device appears as a HA `cover` entity with **Open / Stop / Close** controls. Because the underlying protocols are one-way (no feedback from the motor), the state is **logical** — it reflects the last command sent, not the actual motor position.

Two-code devices (OPEN + CLOSE only, no STOP) are also supported — the STOP button simply has no effect.

## Services

Same services as the original ESPSomfy RTS integration. See [Services wiki](https://github.com/rstrouse/ESPSomfy-RTS-HA/wiki/Services). RF devices respond to standard HA cover services (`cover.open_cover`, `cover.close_cover`, `cover.stop_cover`).

## Events

The integration emits events on the HA event bus for all Somfy RTS commands using event type `espsomfy-rts_event`. Payload:

* `entity_id`, `event_key`, `name`
* `source`: `remote` / `internal` / `group`
* `remote_address`, `source_address`
* `command`: `Up` / `Down` / `My` / `StepUp` / `StepDown` / `Prog` / `My+Up` / `My+Down` / `Up+Down` / `My+Up+Down`

RF devices currently do not emit events (they have no rolling code or remote identification).

## Hardware

- **Firmware**: [QA RF Hub firmware](https://github.com/qa-automacao/QARFHub) (or original [ESPSomfy RTS](https://github.com/rstrouse/ESPSomfy-RTS))
- **Board**: ESP32-S3 DevKitC-1 N16R8 (16 MB flash, 8 MB PSRAM)
- **Radio**: CC1101 module at 433 MHz, connected via SPI (SCK=12, MOSI=11, MISO=13, CSN=10, GDO0/TX=8, GDO2/RX=18)

## Credits

- Original ESPSomfy RTS firmware and HA integration: [@rstrouse](https://github.com/rstrouse)
- QA RF Hub firmware fork and open-protocol RF additions: QA Automação
