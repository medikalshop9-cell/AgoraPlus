# Tech Stack — AGORA+
Always refer to [tech_stack.md](./docs/tech_stack.md) for the allowed versions of FastAPI, Flutter, PostgreSQL, Firebase, Stream Chat, Render, GitHub, Visual Studio Code.
## Architecture
Mobile App (Flutter) → API Server (FastAPI) → PostgreSQL

## Supporting services:
Authentication
Push Notifications
File Storage
Chat Infrastructure

## Frontend Responsibilities
The mobile app handles:
User interface
Navigation
Form input
Displaying events
Displaying announcements
Chat interface
Voting interface
Member directory
Profile management
It communicates with the backend via REST APIs

## Core Technologies
| Layer | Technology | Reason |
|---|---|---|
| Mobile | Flutter | Single codebase iOS + Android |
| Backend | FastAPI | Fast, built-in docs, Python ecosystem |
| Database | PostgreSQL | Reliable, scalable, relational |
| Auth | Firebase Authentication | UM6P accounts, domain restriction |
| Notifications | Firebase Cloud Messaging | Push delivery |
| File Storage | Firebase Storage | Posters, photos, avatars |
| Chat | Stream Chat | Real-time, moderation, encryption |
| Hosting | Render (alt: Railway) | Cloud hosting for FastAPI + PostgreSQL |
| Version Control | GitHub | Source control, CI/CD |
| Dev Editor | Visual Studio Code | |

## API Communication
- REST API
- JSON responses
- HTTPS encryption

## Push Notification Service
Technology:
Firebase Cloud Messaging
-Notification Types
-Notifications will be sent for:
-New announcement
-New event
-Event reminder
-Voting opened
-Pinned message
The backend triggers notifications via API calls.

## File Storage System
Technology:
Firebase Storage
Stored Files
The storage system will host:
Event posters
Event photos
User profile pictures
Files are accessed via secure URLs.

Chat System
To support real-time messaging, a dedicated chat service will be used.

Technology option:

## Stream Chat
Chat Features
-Real-time messaging
-Message history
-Threaded replies
-Admin moderation
-Pinned messages
-User muting
-User banning
Messages should support end-to-end encryption where possible.

## Video Meeting Integration
Events may include live meetings.
Integration platform:
Microsoft Teams
Usage
Admins include a Teams meeting link when creating events.
Inside the app:
Tap "Join Meeting"
↓
Opens Teams meeting

## Security
- HTTPS encryption
- Token-based auth (Azure AD)
- RBAC (admin vs member)
- Domain-restricted login (@um6p.ma)
- Vote duplication prevention

## Authentication System
Technology and Function
Email Authentication
Users authenticate using their university email address
Domain Restriction (@um6p.ma)
The system only accepts emails ending with @um6p.ma
Email Verification (OTP / Magic Link)
A verification code or link is sent to confirm email ownership
Backend Validation
Server checks domain and verification before granting access
Session / JWT Token
After verification, a secure session token is issued for authenticated access
Rate Limiting
Limits repeated login attempts to prevent abuse or bot attacks
Access Control
Only verified UM6P email holders can use the application

User enters email
       ↓
Check domain (@um6p.ma)
       ↓
Send verification code / magic link
       ↓
User verifies email
       ↓
Backend validates request
       ↓
Session token issued
       ↓
User gains access to AGORA+
## Scalability
- Multi-club schema from day one
- Clubs table supports multiple universities (future)
