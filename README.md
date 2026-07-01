# VoiceIsolate — Live Web App

Remove background music from any video. Free. Works on your phone. No install needed.

## How to make it live (GitHub Pages — FREE)

### Step 1: Create a GitHub account (if you don't have one)
- Go to [github.com](https://github.com)
- Sign up with your email. It's free.

### Step 2: Create a new repository
1. Click the green **"New"** button (or go to [github.com/new](https://github.com/new))
2. **Repository name:** `voice-isolate` (or whatever you want)
3. Make it **Public** (required for free GitHub Pages)
4. Check the box **"Add a README file"**
5. Click **"Create repository"**

### Step 3: Upload these files
1. In your new repo, click **"Add file"** → **"Upload files"**
2. Drag and drop ALL files from this folder:
   - `index.html`
   - `manifest.json`
   - `sw.js`
   - `.github/workflows/pages.yml` (create the folders by typing `.github/workflows/pages.yml` in the filename box)
3. Click **"Commit changes"**

### Step 4: Enable GitHub Pages
1. In your repo, click **"Settings"** (tab at the top)
2. On the left sidebar, click **"Pages"**
3. Under **"Build and deployment"**, set **Source** to **"GitHub Actions"**
4. Click **"Save"**

### Step 5: Wait 2 minutes
- GitHub will automatically build and deploy your site
- Go to **"Actions"** tab to see the build progress
- When it's green (✅), your site is live!

### Step 6: Get your live URL
- Your site will be at: `https://YOUR_USERNAME.github.io/voice-isolate/`
- Example: `https://john.github.io/voice-isolate/`
- Open this URL on your phone. It works immediately.

### Step 7: Add to your phone's home screen
- Open the live URL in your phone browser (Chrome, Safari, Samsung Internet)
- Tap the menu (⋮ or ⋯)
- Choose **"Add to Home Screen"** or **"Install"**
- It now looks and works like a real app, offline too!

---

## What this app does

**Drop a video or audio file** → **Choose a mode** → **Get clean voice**

### Two modes:

**1. Full AI Removal** (Best quality)
- Redirects to [VocalRemover.org](https://vocalremover.org) — a free tool that uses AI to perfectly separate voice from music
- Same technology as Capcut's AI
- Completely free, no signup, no install
- Upload your file there, download the "Vocals" track

**2. Fast Voice Boost** (Instant, works offline)
- Runs entirely in your phone browser
- Uses real audio processing: stereo separation, voice EQ, noise gate
- Reduces background music and boosts speech clarity
- Works without internet after first load
- Export as WAV file

---

## Files in this repo

| File | Purpose |
|------|---------|
| `index.html` | The entire app (HTML, CSS, JavaScript all in one) |
| `manifest.json` | PWA manifest — makes it installable like a real app |
| `sw.js` | Service worker — lets it work offline |
| `.github/workflows/pages.yml` | Auto-deploys to GitHub Pages on every change |

---

## Why this is free forever

- GitHub Pages is free for public repos
- No backend server needed
- The app runs in your browser
- The AI processing is done by free third-party tools (VocalRemover.org)
- You own the code. No one can shut it down.

---

## Need help?

If anything breaks or you want changes, just edit `index.html` on GitHub and commit. The site will auto-update in 2 minutes.
