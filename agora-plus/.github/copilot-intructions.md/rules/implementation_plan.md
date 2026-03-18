# Implementation Plan — AGORA+
## Current progress
Follow the roadmap in [implementation_plan.md](./docs/implementation_plan.md).Before starting any task, check the current progress and update it after completing the task.


## Phase 1 — Planning & Design (1–2 weeks)
- Finalize PRD, App Flow, Tech Stack, Frontend Guidelines, Backend Schema
- Wireframes / clickable prototype (Figma / Adobe XD)

## Phase 2 — Backend Setup (2–3 weeks)
- PostgreSQL setup, FastAPI server, Azure AD auth
- API endpoints: User, Club, Event, RSVP, Announcement, Voting, Chat, Notifications
- Firebase Cloud Messaging + Firebase Storage
- RBAC implementation
- Unit tests for endpoints

## Phase 3 — Frontend Development (2–3 weeks)
- Flutter project (iOS + Android)
- All 6 navigation tabs implemented
- Connected to backend APIs

## Phase 4 — Chat & Real-Time Features (1–2 weeks)
- Stream Chat integration
- Real-time messaging, encryption
- Admin moderation
- Event chats auto-deleted after event ends

## Phase 5 — Voting & Election System (1 week)
- Admin creates election
- Anonymous member voting
- Results visible to admins only

## Phase 6 — Testing & QA (1–2 weeks)
- Functional, UI, security, performance testing
- Bug fixes

## Phase 7 — Deployment (1 week)
- Backend to Render/Railway
- App Store + Google Play submission
- Push notification setup for live environment

## Phase 8 — Post-Launch & Maintenance (Ongoing)
- Monitor, collect feedback, plan multi-club expansion, AI features

## MVP vs Full Version
| MVP | Full Version |
|---|---|
| UM6P login, events, RSVP, chat, voting, members, profile, push notifications | Multiple clubs, multiple chat channels, member media uploads, advanced analytics, AI recommendations |

## Total MVP Timeline: ~8–12 weeks
