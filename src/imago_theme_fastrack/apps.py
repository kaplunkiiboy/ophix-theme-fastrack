from django.apps import AppConfig


class ImagoThemeFastrackConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "imago_theme_fastrack"
    verbose_name = "Theme: Fastrack"

    def ready(self):
        from django.db.models.signals import post_migrate
        from django.apps import apps
        # Fire after admin_interface migrations — guarantees the Theme
        # table exists.  The receiver is idempotent: skips if already
        # installed.
        post_migrate.connect(
            _install_on_migrate,
            sender=apps.get_app_config("admin_interface"),
        )


def _install_on_migrate(sender, **kwargs):
    from ophix_theme_tools.utils import install_bundled_theme
    from django.apps import apps
    install_bundled_theme(apps.get_app_config("imago_theme_fastrack"))
