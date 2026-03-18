# AGORA+

Mobile app for UM6P club members — starting with Africa Consulting Club (ACC).

## Purpose
- Share announcements
- RSVP to events
- Chat securely
- Vote in elections
- Manage profiles

## Multi-club Ready
Schema and architecture support multiple clubs from day one.

## Tech Stack
| Layer | Tech |
|---|---|
| Mobile | Flutter (iOS + Android) |
| Backend | FastAPI (Python) |
| Database | PostgreSQL |
| Auth | Firebase Authentication |
| Notifications | Firebase Cloud Messaging |
| Storage | Firebase Storage |
| Chat | Stream Chat |
| Hosting | Render |

## Docs
All planning documents are in `/docs` and mirrored into `/.cursor/rules`.

| Doc | Purpose |
|---|---|
| `AIrules.md` | AI coding workflow and phase rules |
| `app_flow.md` | Screen navigation and user flows |
| `backend_schema.md` | Full PostgreSQL schema |
| `frontend_guidelines.md` | UI/UX rules, typography, colors |
| `tech_stack.md` | Technology decisions and architecture |
| `implementation_plan.md` | Phase-by-phase build plan |

## MVP Timeline
~8–12 weeks across 7 phases. See `docs/implementation_plan.md`.

## Getting Started

### Backend
```bash
cd backend
cp .env.example .env
# Fill in .env values
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend
```bash
cd frontend/agora_app
flutter pub get
flutter run
```
