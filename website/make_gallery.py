from pathlib import Path

gallery = Path.home() / "CommunityArchive/website/gallery/KetevanPhotos"
outfile = Path.home() / "CommunityArchive/website/gallery.html"

images = sorted(
    [f for f in gallery.iterdir()
     if f.suffix.lower() in [".jpg", ".jpeg", ".png"]]
)

html = """
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Ketevan Theatre Collection</title>

<style>

body{
    font-family:Arial;
    background:#f5f5f5;
    margin:20px;
}

h1{
    color:#1f4e79;
}

.toolbar{
    background:white;
    padding:15px;
    border-radius:8px;
    margin-bottom:20px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fill,minmax(180px,1fr));
    gap:18px;
}

.card{
    background:white;
    border-radius:8px;
    padding:10px;
    box-shadow:0 2px 6px rgba(0,0,0,.2);
    text-align:center;
}

img{
    width:160px;
    height:160px;
    object-fit:cover;
    border-radius:6px;
}

.name{
    font-size:12px;
    margin-top:6px;
    word-break:break-word;
}

</style>

</head>
<body>

<h1>🎭 Ketevan Theatre Collection</h1>

<div class="toolbar">

Collection:
<b>Ketevan Theatre</b>

&nbsp;&nbsp;&nbsp;

Privacy:
<select>
<option>Family</option>
<option>Community</option>
<option>Public</option>
<option>Restricted</option>
</select>

<label style="margin-left:20px;">
<input type="checkbox">
Opt out of AI
</label>

<button style="float:right;">
Import Selected
</button>

</div>

<div class="grid">
"""

for img in images:

    rel = "gallery/KetevanPhotos/" + img.name

    html += f"""
<div class="card">
<input type="checkbox"><br>
<a href="{rel}" target="_blank">
<img src="{rel}">
</a>
<div class="name">{img.name}</div>
</div>
"""

html += """
</div>

</body>
</html>
"""

outfile.write_text(html,encoding="utf-8")

print("Gallery created:",outfile)
print("Images:",len(images))
