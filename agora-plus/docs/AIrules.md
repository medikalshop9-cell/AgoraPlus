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

## 7. Dependency Rules
- Backend APIs must exist before frontend integrates
- DB schema must exist before API endpoints
- Auth must exist before member-related features
- Chat features cannot proceed before chat service integration

## 8. Do / Don't
**Do:** Stick to phase order, summarise progress, ask plain-English questions, provide modular reusable code.
**Don't:** Mix phases, assume user preferences, skip RBAC or security checks, deliver code without context.

## Development Workflow (Strict Order)
## Phase 0: Freeze the docs
Before coding, finish and lock:
• PRD
• App Flow
• Tech Stack
• Frontend Guidelines
• Backend Schema
• Implementation Plan
• AIrules.md

## Phase 1: Setup
Create:
• repo structure
• Flutter app starter
• FastAPI backend starter
• environment files
• basic configs

## Phase 2: Authentication
Build:
• Microsoft login
• UM6P email restriction
• role setup
• member profile creation

## Phase 3: Core data
Build:
• clubs
• users
• announcements
• events
• RSVPs

## Phase 4: Frontend screens
Build:
• Home
• Events
• Community
• Voting
• Members
• Profile

## Phase 5: Chat
Build:
• main chat
• event discussion chat
• moderation tools

## Phase 6: Voting
Build:
• election creation
• anonymous voting
• results

## Phase 7: Notifications
Build:
• push notifications
• event reminders
• vote alerts

## Phase 8: Testing
Test:
• auth
• permissions
• IDOR
• rate limiting
• flows
• edge cases

## Phase 9: Deploy
Then:
• backend on Render
• mobile build
• store deployment later