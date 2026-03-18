# App Flow Document — AGORA+

## 1. Entry Point
- App checks auth status
- Logged in → Home Screen
- Not logged in → Login Screen
- Auth via Microsoft (UM6P accounts)

## 2. Authentication Flow
- Sign in with Microsoft → domain verified (@um6p.ma) → account created → Member Directory → app entry

## 3. First-Time Setup
- Profile photo (optional), Major, Year of study → Home Screen

## 4. Main Navigation (Bottom Tabs)
Home | Events | Community | Voting | Members | Profile

## 5. Home Screen
- Latest Announcements
- Upcoming Events
- Past Events
- Event Photo Decks

## 6. Events Tab
- Upcoming / Past Events
- Event Detail: poster, description, date, time, location, RSVP, calendar, Teams link, discussion, attendees
- Event Discussion Chat (removed when event ends)

## 7. Community Tab
- ACC General Chat
- Send, reply, read messages
- Admin: delete, mute, ban, pin
- End-to-end encrypted

## 8. Voting Tab
- Active / Past Elections
- Election Detail: position, candidates, deadline, vote button
- Anonymous vote, one vote per user

## 9. Members Tab
- Searchable directory: Admins + Members
- Member profile: name, email, major, year, photo, role

## 10. Profile Tab
- Account (edit photo, major, year)
- Settings (notifications, privacy, language)
- Help (FAQ, contact, report)
- Switch User / Logout

## 11. Push Notifications
- Tapping redirects to relevant screen

## 12. Admin Actions
- Create announcements, events, upload photos, start elections, moderate chat

## 13. Error Handling
- Invalid domain → access denied
- RSVP full → RSVP disabled
- Duplicate vote → blocked
