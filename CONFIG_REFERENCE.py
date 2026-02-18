"""
VoiceFix 360 - Configuration & Usage Reference
================================================

This file provides quick reference for configuration, dependencies, and usage.
"""

# ============================================================================
# 1. INSTALLATION COMMANDS
# ============================================================================

"""
# Basic setup
pip install -r requirements.txt

# Windows-specific (if PyAudio fails)
pip install pipwin
pipwin install PyAudio

# Run the app
streamlit run app.py
"""

# ============================================================================
# 2. SUPPORTED LANGUAGES & CODES
# ============================================================================

LANGUAGES = {
    "en": "English (English)",
    "hi": "Hindi (हिंदी)",
    "or": "Odia (ଓଡିଆ)"
}

# ============================================================================
# 3. FEATURE FLAGS (Configured in app.py)
# ============================================================================

FEATURES = {
    "voice_recording": True,        # Real-time audio recording
    "translator": True,             # Multi-language translator
    "language_detection": True,     # Auto language detection
    "ticket_history": True,         # Store ticket history
    "export_json": True,            # Export as JSON
    "export_text": True,            # Export as text
    "confidence_scores": True,      # Show confidence metrics
    "dark_mode": True,              # Dark theme enabled
    "analytics": True,              # Show analytics tab
}

# ============================================================================
# 4. API CONFIGURATION
# ============================================================================

API_CONFIG = {
    "model": "gemini-2.0-flash-001",
    "voice_timeout": 15,            # seconds
    "max_retries": 3,
    "quote_check_enabled": True,
    "fallback_mode": True,          # Use backup if API fails
}

# ============================================================================
# 5. AUDIO RECORDING SETTINGS
# ============================================================================

AUDIO_CONFIG = {
    "sample_rate": 16000,           # Hz
    "channels": 1,                  # Mono
    "chunk_size": 2048,
    "format": "wav",
    "max_duration": 15,             # seconds
    "silence_threshold": 0.03,
}

# ============================================================================
# 6. LANGUAGE DETECTION SETTINGS
# ============================================================================

LANGUAGE_DETECTION = {
    "enable_auto_detect": True,
    "confidence_threshold": 0.7,
    "fallback_language": "en",
    "supported_langs": ["en", "hi", "or"],
}

# ============================================================================
# 7. UI CUSTOMIZATION
# ============================================================================

UI_CONFIG = {
    "primary_color": "#4CAF50",     # Green
    "secondary_color": "#2E7D32",   # Dark Green
    "error_color": "#FF5252",       # Red
    "warning_color": "#FFEB3B",     # Yellow
    "success_color": "#4CAF50",     # Green
    "info_color": "#2196F3",        # Blue
    "theme": "dark",                # dark or light
    "animation_enabled": True,
    "sidebar_visible": True,
    "max_ticket_history": 50,
}

# ============================================================================
# 8. TRANSLATION SETTINGS
# ============================================================================

TRANSLATION = {
    "provider": "gemini",
    "auto_translate_to_english": True,
    "preserve_formatting": True,
    "technical_jargon_handling": True,
}

# ============================================================================
# 9. ERROR HANDLING & FALLBACKS
# ============================================================================

ERROR_HANDLING = {
    "use_backup_on_quota_exceeded": True,
    "silent_fail_microphone": False,
    "retry_on_api_error": True,
    "max_retries": 3,
    "retry_delay": 2,               # exponential backoff
    "show_detailed_errors": True,
}

# ============================================================================
# 10. QUICK START EXAMPLES
# ============================================================================

"""
EXAMPLE 1: Using Voice Recording
---------------------------------
1. Click "Quick Support" tab
2. Upload an error screenshot
3. Click "START REC" button
4. Speak in Hindi, Odia, or English
5. Click "GENERATE TICKET & RESOLVE"
6. Ticket is created with auto-translated content

EXAMPLE 2: Using Translator
----------------------------
1. Click "Translator Studio" tab
2. Paste text in any language
3. Leave source as "Auto-detect"
4. Select target language
5. Click "Translate Now"
6. Get instant translation

EXAMPLE 3: Exporting Tickets
-----------------------------
1. After ticket is generated
2. Click "Export as JSON" or "Export as Text"
3. Download button appears
4. Save file to share with support team

EXAMPLE 4: Viewing Analytics
-----------------------------
1. Click "Advanced Analytics" tab
2. See total tickets created
3. View session statistics
4. Check ticket history
5. Monitor API status
"""

# ============================================================================
# 11. TROUBLESHOOTING QUICK GUIDE
# ============================================================================

TROUBLESHOOTING = {
    "microphone_not_found": {
        "solution": "Enable microphone permissions in system settings",
        "fallback": "Use manual text input instead"
    },
    "api_quota_exceeded": {
        "solution": "Upgrade plan at https://aistudio.google.com/app/apikey",
        "fallback": "Wait 24 hours for quota reset"
    },
    "poor_speech_recognition": {
        "solution": "Speak clearly in a quiet environment",
        "fallback": "Type text manually"
    },
    "translation_fails": {
        "solution": "Check internet connection",
        "fallback": "Use manual translator"
    },
}

# ============================================================================
# 12. PERFORMANCE OPTIMIZATION
# ============================================================================

OPTIMIZATION = {
    "cache_enabled": True,
    "compress_images": True,
    "max_image_size": 5242880,      # 5MB
    "lazy_load_tabs": True,
    "session_cleanup_interval": 3600,  # 1 hour
}

# ============================================================================
# 13. KEYBOARD SHORTCUTS
# ============================================================================

SHORTCUTS = {
    "create_ticket": "Ctrl+Enter",
    "clear_form": "Ctrl+C",
    "start_recording": "Ctrl+R",
    "translate": "Ctrl+T",
}

# ============================================================================
# 14. SUPPORTED FILE FORMATS
# ============================================================================

SUPPORTED_FORMATS = {
    "image": ["jpg", "jpeg", "png"],
    "audio": ["wav", "mp3", "ogg"],
    "export": ["json", "txt", "csv"],
}

# ============================================================================
# 15. CONTACT & SUPPORT
# ============================================================================

SUPPORT_INFO = {
    "team": "Team VaniVerse",
    "event": "GIET Ghangapatna Hackfest 2.0",
    "version": "2.0 Enterprise Edition",
    "last_updated": "February 2026",
}
