"""Small wrappers for Android intents with desktop fallbacks."""

from __future__ import annotations

import webbrowser

from kivy.core.clipboard import Clipboard
from kivy.utils import platform

IS_ANDROID = platform == "android"


def copy_text(text: str) -> None:
    Clipboard.copy(text)


def open_url(url: str) -> bool:
    if not IS_ANDROID:
        return webbrowser.open(url)
    from jnius import autoclass

    Intent = autoclass("android.content.Intent")
    Uri = autoclass("android.net.Uri")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
    try:
        PythonActivity.mActivity.startActivity(intent)
        return True
    except Exception:
        return False


def open_app(package: str) -> bool:
    """Open an installed app by package, or its Play Store page when missing.

    Uses an explicit launcher intent so Android 11 package visibility rules do
    not require a <queries> manifest entry.
    """
    if not IS_ANDROID:
        return False
    from jnius import autoclass

    Intent = autoclass("android.content.Intent")
    PythonActivity = autoclass("org.kivy.android.PythonActivity")
    intent = Intent(Intent.ACTION_MAIN)
    intent.addCategory(Intent.CATEGORY_LAUNCHER)
    intent.setPackage(package)
    intent.addFlags(Intent.FLAG_ACTIVITY_NEW_TASK)
    try:
        PythonActivity.mActivity.startActivity(intent)
        return True
    except Exception:
        return open_url(f"market://details?id={package}") or open_url(
            f"https://play.google.com/store/apps/details?id={package}"
        )
