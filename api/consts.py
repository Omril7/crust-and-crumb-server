import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

ERROR_REDIRECT_HTML = """
<!doctype html>
<html lang="en">
   <head>
      <meta charset="utf-8" />
      <title>Crust & Crumb — Error</title>
      <meta name="viewport" content="width=device-width, initial-scale=1" />
      <style>
         :root{
         --bg:#0f172a; --card:#111827; --text:#e5e7eb; --muted:#9ca3af;
         --accent:#22c55e; --accent-2:#16a34a; --ring:0 0 0 1px rgba(255,255,255,.05), 0 10px 25px rgba(0,0,0,.35);
         }
         @media (prefers-color-scheme: light){
         :root{ --bg:#f9fafb; --card:#ffffff; --text:#111827; --muted:#6b7280; --accent:#16a34a; --accent-2:#15803d; }
         }
         html, body { height:100%; margin:0; }
         body {
         display:grid; place-items:center; background:var(--bg); color:var(--text);
         font:16px/1.5 system-ui, sans-serif;
         }
         .card {
         background:var(--card); border-radius:20px; padding:32px; text-align:center;
         width:min(500px, 92vw); box-shadow:var(--ring);
         }
         h1 { font-size:2rem; margin:0 0 10px; }
         p { margin:0 0 18px; color:var(--muted); }
         .btn {
         display:inline-block; padding:12px 20px; border-radius:12px;
         text-decoration:none; color:white; font-weight:600; font-size:1rem;
         background:linear-gradient(90deg, var(--accent), var(--accent-2));
         box-shadow:0 8px 22px rgba(34,197,94,.28);
         }
         .logo {
         font-weight:800; font-size:2.2rem; color:var(--accent); margin-bottom:12px;
         }
      </style>
   </head>
   <body>
      <main class="card">
         <div class="logo">⚠️</div>
         <h1>Oops! Something went wrong</h1>
         <p>We couldn’t find this page. But you can go back to Crust &amp; Crumb:</p>
         <a class="btn" href="https://crust-and-crumb.vercel.app/">Go to Crust &amp; Crumb</a>
      </main>
   </body>
</html>
"""
