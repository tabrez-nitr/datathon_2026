# Database

## Core Tables

- FIR
- Victim
- Accused
- PoliceStation
- Officer
- Arrest
- Court
- District
- CrimeCategory

## Relationships

FIR
- has many Victims
- has many Accused
- belongs to Police Station

Accused
- may appear in multiple FIRs

Victim
- may appear in multiple FIRs

Officer
- investigates FIRs

## Future Tables

- Conversation History
- AI Logs
- Audit Logs