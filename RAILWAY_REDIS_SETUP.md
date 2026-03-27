# Setting up Redis on Railway

To add Redis to your existing Night Watchman project on Railway:

1.  **Open your project** in the [Railway Dashboard](https://railway.app/dashboard).
2.  Click the **"New"** button (or "Create" / "+").
3.  Select **"Database"**.
4.  Choose **"Redis"**.
5.  This will provision a new Redis service in your project.

### Connecting the Bot

1.  Once Redis is deployed, click on the **Redis** service card.
2.  Go to the **"Variables"** or **"Connect"** tab.
3.  Find the `REDIS_URL` variable (it looks like `redis://default:password@host:port`).
4.  Copy this value.
5.  Go to your **Night Watchman Bot** service.
6.  Go to the **"Variables"** tab.
7.  Add a new variable:
    *   **Key**: `REDIS_URL`
    *   **Value**: Paste the Redis URL you copied (e.g., `${{Redis.REDIS_URL}}` if using Railway's reference syntax, or the full string).
8.  Railway will automatically redeploy your bot with the new variable.

### Local Development

If you are running the bot locally:
1.  Install Redis on your Mac: `brew install redis`
2.  Start Redis services: `brew services start redis`
3.  Add `REDIS_URL=redis://localhost:6379/0` to your local `.env` file.
