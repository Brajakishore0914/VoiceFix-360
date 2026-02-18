# VoiceFix 360 - Enterprise AI Support System

## 🌟 Features

### ✨ Advanced Voice Recording & Recognition
- **Real-time Audio Input**: 15-second recording capability with voice detection
- **Multi-Language Support**: English, Hindi, Odia
- **Automatic Language Detection**: AI-powered language identification
- **Background Noise Adjustment**: Automatic ambient noise filtering

### 🔄 Advanced Translator Studio
- **Multi-Language Translation**: Hindi ↔ Odia ↔ English
- **AI-Powered Accuracy**: Uses Gemini 2.0 for precise translation
- **Live Translation**: Real-time conversion with confidence scores
- **Context-Aware**: Understands technical jargon and local expressions

### 🚀 Interactive Features
- **3-Tab Interface**: Quick Support | Translator | Analytics
- **Real-time Progress Tracking**: Visual feedback during processing
- **Ticket History**: Track all created support tickets
- **Export Options**: Download tickets as JSON or TXT
- **Dark/Light Theme Toggle**: Customizable UI

### 📊 Advanced Analytics
- **Ticket Management**: Complete ticket tracking system
- **Confidence Scores**: Language detection accuracy metrics
- **Session Statistics**: Monitor API usage and performance
- **Error Logging**: Detailed error handling and fallback mechanisms

---

## 🔧 Installation & Setup

### Step 1: Clone/Download Project
```bash
cd c:\Users\tapas\OneDrive\Desktop\VoiceFix_Project
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note for Windows users**: If PyAudio fails to install, use:
```bash
pip install pipwin
pipwin install PyAudio
```

### Step 3: Set Up Google API Key
1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Create a new API key for Generative AI
3. In `app.py`, replace `"PASTE_YOUR_API_KEY_HERE"` with your actual API key:
```python
os.environ["GOOGLE_API_KEY"] = "your-actual-api-key-here"
```

### Step 4: Run the Application
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

---

## 📖 How to Use

### Quick Support Tab 🚀
1. **Upload Screenshot**: Capture and upload your system error
2. **Record Voice**: Click "START REC" to record your issue (supports Hindi, Odia, English)
   - OR type manually in English, Hindi, or Odia
3. **Auto-Detection**: System automatically detects your language
4. **Generate Ticket**: Click "GENERATE TICKET & RESOLVE"
5. **Get Solution**: AI provides error code, severity, and solution steps
6. **Export**: Download ticket as JSON or TXT format

### Translator Studio 🔄
1. Enter text in source language
2. Select source language (Auto-detect recommended)
3. Choose target language (English, Hindi, or Odia)
4. Click "Translate Now"
5. Get instant, accurate translation

### Advanced Analytics 📊
- View all tickets created in session
- Check API connection status
- Monitor total tickets and session stats
- Review ticket history with timestamps

---

## 🎯 Supported Languages

| Language | Code | Support |
|----------|------|---------|
| English  | en   | ✅ Full |
| Hindi    | hi   | ✅ Full |
| Odia     | or   | ✅ Full |

---

## 🔐 Security & Privacy

- **Local Processing**: Audio files are temporarily stored only during processing
- **Auto-Cleanup**: Temporary files deleted after processing completes
- **No Data Storage**: No user data is permanently stored
- **API Security**: Secure connection to Google Generative AI

---

## ⚙️ Advanced Configuration

### Custom Settings (in sidebar)
- **Theme**: Dark Mode / Light Mode
- **Show Ticket History**: Enable/disable history display
- **Show Translator**: Enable/disable translator tab
- **Show Confidence Scores**: Display language detection confidence

---

## 🐛 Troubleshooting

### Issue: Microphone not detected
**Solution**: 
- Check microphone permissions in system settings
- Use manual text input instead
- Restart the application

### Issue: Translation fails
**Solution**:
- Check internet connection
- Verify Google API key is valid
- Try again with shorter text

### Issue: Speech recognition doesn't work
**Solution**:
- Ensure you have a working microphone
- Speak clearly and slowly
- Check audio input levels
- Try recording in a quiet environment

### Issue: API Quota Exceeded
**Solution**:
- Upgrade your plan at Google AI Studio
- Wait for quota reset (usually 24 hours)
- Check https://aistudio.google.com/app/apikey for limits

---

## 🚀 Performance Tips

1. **Use Clear Audio**: Record in quiet environments for better recognition
2. **Keep Uploads Small**: Use compressed images for faster processing
3. **Check Internet**: Ensure stable internet connection
4. **Clear History**: Regular cleanup for optimal performance

---

## 📝 Example Usage

```
1. Upload screenshot showing: "CRITICAL_PROCESS_DIED error"
2. Record in Hindi: "Mere computer ko crash ka issue hai"
3. System detects: Language = Hindi
4. AI translates and processes
5. Ticket created with: Error code, severity, and solution
6. Export and share with support team
```

---

## 🤝 Support

For issues or questions:
1. Check the "How to Use" section in side Settings
2. Review Troubleshooting section above
3. Verify API key is correctly configured
4. Ensure all dependencies are installed

---

## 📄 License

This project is part of GIET Ghangapatna Hackfest 2.0

**Created by**: Team VaniVerse

---

## 🎉 Features Coming Soon

- Multi-image analysis
- Video error recording
- Email ticket delivery
- Slack integration
- Mobile app support
- Offline mode
- Custom language models

---

**Version**: 2.0 Enterprise Edition
**Last Updated**: February 2026
