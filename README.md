# Inet Usage Counter Test

When the script starts, the counter is initialized to 0.

## Mac OS

Option to run as a daemon process.

#### com.ajhenri.inet_usage_test.plist
```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>EnvironmentVariables</key>
        <dict>
        <key>INET_USAGE_PATH</key>
        <string>/Users/youruser/Documents/inet_usage_test</string>
        </dict>
        <key>Label</key>
        <string>com.ajhenri.inet_usage_test</string>
        <key>ProgramArguments</key>
        <array>
            <string>/Users/youruser/Documents/inet_usage_test/venv/bin/python3</string>
            <string>/Users/youruser/Documents/inet_usage_test/inet_usage_test.py</string>
        </array>
        <key>RunAtLoad</key>
        <true/>
        <key>KeepAlive</key>
        <false/>
        <key>LaunchOnlyOnce</key>        
        <true/>
        <key>StandardOutPath</key>
        <string>/Users/youruser/Documents/inet_usage_test/logs/output.log</string>
        <key>StandardErrorPath</key>
        <string>/Users/youruser/Documents/inet_usage_test/logs/error.log</string>
        <key>UserName</key>
        <string>youruser</string>
        <key>GroupName</key>
        <string>yourgroup</string>
    </dict>
</plist>
```

### To run
`sudo launchctl load com.ajhenri.inet_usage_test.plist`

### To stop
`sudo launchctl unload com.ajhenri.inet_usage_test.plist`