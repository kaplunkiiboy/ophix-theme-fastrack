# ophix-theme-fastrack

**Fastrack** — Fastrack branding theme for Ophix servers.

Installs the Fastrack theme into the Django admin on `migrate`. The theme installs
inactive — activate it with:

```bash
ophix-manage set_theme Fastrack
```

Or via **Admin Interface → Themes** in the admin UI.

## Installation

```bash
pip install ophix-theme-fastrack
ophix-manage migrate
ophix-manage set_theme Fastrack
```

To install this theme you will also need [Ophix Theme Tools](https://github.com/ophixproject/ophix-theme-tools).
