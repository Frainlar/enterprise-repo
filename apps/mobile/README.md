# Enterprise Mobile App

This Flutter project targets Web, Android, and iOS. Platform folders were not
checked into version control. Run the following command to create them:

```bash
flutter create . --platforms=android,ios,web
```

Afterwards you can build the web app with PWA support:

```bash
flutter build web
```

The `web/` directory already contains a service worker (`pwabuilder-sw.js`) and
manifest generated via PWABuilder. The service worker is registered in
`web/index.html`. Icon URLs are placeholders pointing to `via.placeholder.com`.
