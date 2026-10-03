import re

with open('src/App.tsx', 'r') as f:
    app_code = f.read()

# Replace the video tag with the robust inline handlers
new_video_tag = """
        <video
          autoPlay
          muted
          defaultMuted={true}
          loop
          playsInline
          onCanPlay={(e) => e.currentTarget.play().catch(() => {})}
          onLoadedData={(e) => e.currentTarget.play().catch(() => {})}
          className="absolute inset-0 w-full h-full object-cover"
          src="/olesya-bg.mp4"
        />
"""

app_code = re.sub(
    r'<video[^>]+src="/olesya-bg\.mp4"\s*/>',
    new_video_tag.strip(),
    app_code,
    flags=re.DOTALL
)

with open('src/App.tsx', 'w') as f:
    f.write(app_code)
