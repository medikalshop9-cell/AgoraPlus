# Backend Schema — AGORA+
Database: PostgreSQL

## Tables

### clubs
| Field | Type | Description |
|---|---|---|
| id | UUID PK | Unique club ID |
| name | Text | Club name |
| description | Text | Short description |
| created_at | Timestamp | |
| updated_at | Timestamp | |

### users
| Field | Type | Description |
|---|---|---|
| id | UUID PK | |
| email | Text | UM6P email |
| name | Text | Full name |
| major | Text | Academic major |
| year_of_study | Int | |
| profile_photo_url | Text | Optional |
| role | Enum | 'admin' or 'member' |
| club_id | UUID FK | |
| created_at | Timestamp | |
| updated_at | Timestamp | |

### announcements
id, club_id (FK), admin_id (FK), title, description, poster_url, created_at

### events
id, club_id (FK), admin_id (FK), title, description, date, location, teams_link, max_attendees, poster_url, created_at, updated_at

### event_rsvps
id, event_id (FK), user_id (FK), rsvp_status (Enum: yes/no/maybe/cancelled), created_at

### voting
id, club_id (FK), admin_id (FK), position, start_date, end_date, created_at, updated_at

### candidates
id, vote_id (FK), name, profile_photo_url

### vote_records
id, vote_id (FK), candidate_id (FK), user_id (FK — internal validation only), created_at

### chat_rooms
id, club_id (FK), event_id (FK nullable), name, created_at

### chat_messages
id, room_id (FK), user_id (FK), message, created_at, pinned (bool), deleted (bool), muted_until (Timestamp)

### event_photos
id, event_id (FK), admin_id (FK), photo_url, created_at

### notifications
id, user_id (FK), type (Enum: announcement/event/voting/chat), title, message, read (bool), created_at

## Key Relationships
- Clubs → Users: one-to-many
- Clubs → Events: one-to-many
- Events → RSVPs: one-to-many
- Clubs → Voting → Candidates: one-to-many
- Voting → Vote_Records: one-to-many
- Clubs → Chat Rooms → Chat Messages: one-to-many

## Backend (FastAPI Implementation)
-Middleware or dependency
-Example tools: slowapi, redis-based limiter

## Security: Row-Level Access Rules
- Users can only access data from their own club
- Users can only edit their own profile
- Only admins can:
 - create/update/delete events
 - post announcements
 - manage users

## Backend (PostgreSQL / API)
• Enforced via:
• SQL queries (WHERE club_id = current_user.club_id)
• Optional: PostgreSQL RLS policies
Every endpoint must check:
if event.club_id != current_user.club_id:
   raise HTTPException(status_code=403)