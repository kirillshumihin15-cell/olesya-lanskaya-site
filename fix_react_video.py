import re

with open('src/App.tsx', 'r') as f:
    app_code = f.read()

# Replace the video tag with dangerouslySetInnerHTML
new_video_tag = """
        <div 
          className="absolute inset-0 w-full h-full"
          dangerouslySetInnerHTML={{
            __html: `
              <video
                autoplay
                loop
                muted
                playsinline
                class="w-full h-full object-cover"
                style="pointer-events: none;"
              >
                <source src="/olesya-bg.mp4" type="video/mp4" />
              </video>
            `
          }}
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
