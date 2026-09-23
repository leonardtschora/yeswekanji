# OVH self-hosting path, time estimate

Asked in the brief as the fallback. Estimated for an agent doing the work with a
human clicking through OVH's console. Not the recommended path for the prototype.

| Step | Agent time | Wall-clock waits |
|---|---|---|
| a) Order a VPS, SSH key, firewall, non-root user, unattended upgrades | 30 to 45 min | VPS provisioning 5 to 15 min |
| b) Install Docker, write Dockerfile for the Streamlit app, `docker compose up` | 30 min | image pull 2 min |
| c) Write the page. If Streamlit: none extra. If plain HTML/JS: 1 to 2 h for grid, flip, audio | 0 to 2 h | |
| d) Expose: DNS A record, Caddy reverse proxy with automatic TLS, health check | 45 min | DNS propagation up to a few hours |
| Total | 2.5 to 4 h | plus DNS |

Ongoing: OS updates, certificate renewal (automatic with Caddy), monitoring.
About 4 EUR/month for the smallest VPS.

When it becomes worth it: custom domain, private beta with auth, or when the
sleep-after-12h of the free clouds hurts.
