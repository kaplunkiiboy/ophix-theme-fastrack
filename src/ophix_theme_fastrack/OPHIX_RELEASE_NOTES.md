# Ophix Theme Fastrack Release Notes

## 2026.05.30.01

- Standardised theme package media layout to `media/<field>/<filename>` (flat). The previous
  deep layout (`media/admin-interface/themes/<name>/<field>/<filename>`) was redundant since
  `install_bundled_theme` constructs the destination path independently. Requires
  `ophix-admin-interface>=2026.05.30.04`.

## 2026.05.19.01

- Added `OPHIX_RELEASE_NOTES.md` for release notes delivery.
