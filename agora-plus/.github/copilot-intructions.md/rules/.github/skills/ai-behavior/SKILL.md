# AIrules.md — AGORA+

## 1. Project Context
- **Project Name:** AGORA+
- **Purpose:** Mobile app for ACC (Africa Consulting Club), Africa Business Unit-Junior Entreprise, CIC and ISC members at UM6P.
- **Target Users:** Students with @um6p.ma email accounts
- **Design:** Multi-club ready for future expansion
- **Platform:** Mobile (iOS + Android)
- **Primary Tech Stack:** Flutter, FastAPI, PostgreSQL, Firebase, Microsoft Azure AD, Stream Chat

## 2. AI Coding Workflow Rules
- Plan → Complete one phase → Move to next
- Do not mix phases
- Always produce MVP first, then extend features
- After completing any task or code block: summarise what was done, how it integrates, what is next
- Ask in plain English; number or bullet suggestions
- Always confirm assumptions before coding

## 3. Phase Hierarchy (Strict)
1. Planning & Design
2. Backend Setup
3. Frontend MVP
4. Chat Integration
5. Voting System
6. Testing & QA
7. Deployment
8. Post-Launch / Advanced Features

## 4. AI Interaction Rules
- Ask specific clarifying questions when info is missing
- Summarise after each coding session
- Avoid assumptions on user preferences
- Clearly separate suggestions from mandatory instructions

## 5. Testing & Quality
- Write code with testable functions
- Include unit tests for Python and Dart
- Provide a test plan when testing is required

## 6. Security Constraints
- Only @um6p.ma emails can authenticate
- RBAC: admin vs member
- Votes must remain anonymous
- Chats must support end-to-end encryption
- No sensitive info stored in plaintext
- Implement API rate limiting:
- Login: max 5 requests/minute per IP
- Chat: max 20 messages/minute per user
- RSVP/Voting: prevent rapid repeated actions
 
## 7. Dependency Rules
- Backend APIs must exist before frontend integrates
- DB schema must exist before API endpoints
- Auth must exist before member-related features
- Chat features cannot proceed before chat service integration

## 8. Do / Don't
**Do:** Stick to phase order, summarise progress, ask plain-English questions, provide modular reusable code.
**Don't:** Mix phases, assume user preferences, skip RBAC or security checks, deliver code without context.

## 9. Hierarchical / Dependency Rules OR Security Constraints
Add: 
 - Enforce row-level security:
 - All queries must filter by club_id
 - Never return data across clubs

## IDOR (Insecure Direct Object Reference Protection)
Prevent IDOR vulnerabilities:
 - Never trust IDs from frontend
 - Always verify ownership:
   - user belongs to club
   - user has access to resource