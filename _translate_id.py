#!/usr/bin/env python3
"""Bulk chrome translation for id.html - EN -> Bahasa Indonesia.
Keeps prompts (inside .prompt divs) in English since the free Copilot Chat handles both.
Translates: titles, headings, tab labels, scenario callouts, leads, notes, reality checks.
"""
import re
from pathlib import Path

p = Path(__file__).parent / "id.html"
h = p.read_text(encoding="utf-8")

R = [
    # Title tag & hero
    ("<title>Contoso Beauty Innovation &#183; M365 Copilot Immersion</title>",
     "<title>Contoso Beauty Innovation &#183; Imersi M365 Copilot</title>"),
    ("Microsoft 365 Copilot &#183; Admin Team Immersion",
     "Microsoft 365 Copilot &#183; Imersi Tim Admin"),
    ("Workshop Edition &#183; 2026", "Edisi Workshop &#183; 2026"),
    ("4 Exercises + Bonus", "4 Latihan + Bonus"),
    ("One workday, one Board EA, four Copilot Chat moments",
     "Satu hari kerja, satu EA Direksi, empat momen Copilot Chat"),
    ("A hands-on immersion for the Contoso Beauty Innovation Admin Team, built around Bu Sari Wijayanti, Executive Assistant to the Board. Every prompt is copy-and-paste ready. Every exercise is grounded on the sample files. Free Copilot Chat plus the Word, Excel, and PowerPoint Agents only - no paid Copilot licence required.",
     "Imersi langsung untuk Tim Admin Contoso Beauty Innovation, berpusat pada Bu Sari Wijayanti, Executive Assistant Direksi. Setiap prompt siap copy-paste. Setiap latihan berbasis file contoh. Hanya Copilot Chat gratis plus Agen Word, Excel, dan PowerPoint - tidak memerlukan lisensi Copilot berbayar."),

    # Tab labels (sidebar/nav)
    (">Start<", ">Mulai<"),
    (">The Story<", ">Kisahnya<"),
    (">Overview<", ">Ringkasan<"),
    (">Sample Files<", ">File Contoh<"),
    (">Bonus<", ">Bonus<"),
    (">Ex 1 · ", ">Latihan 1 · "),
    (">Ex 2 · ", ">Latihan 2 · "),
    (">Ex 3 · ", ">Latihan 3 · "),
    (">Ex 4 · ", ">Latihan 4 · "),
    ("Morning Brief", "Ringkasan Pagi"),
    ("Word Agent", "Agen Word"),
    ("Excel Agent", "Agen Excel"),
    ("PowerPoint Agent", "Agen PowerPoint"),

    # Common section headers
    (">Exercise 1 · ", ">Latihan 1 · "),
    (">Exercise 2 · ", ">Latihan 2 · "),
    (">Exercise 3 · ", ">Latihan 3 · "),
    (">Exercise 4 · ", ">Latihan 4 · "),

    # Bonus
    ("<small>Five practical additions - click any card</small>",
     "<small>Lima tambahan praktis - klik kartu mana saja</small>"),
    ("Bonus Tab", "Tab Bonus"),
    (">Bonus content.</b> Use these when there is extra time, or when someone in the room asks the question. Click a card to open the full walkthrough.",
     ">Konten bonus.</b> Gunakan saat ada waktu lebih atau saat ada yang bertanya. Klik kartu untuk membuka panduan lengkap."),

    # Reality/scenario/check callout labels (bold)
    (">The scenario.</b>", ">Skenarionya.</b>"),
    (">Reality check.</b>", ">Cek realita.</b>"),
    (">The check.</b>", ">Pengecekan.</b>"),
    (">The moment.</b>", ">Momennya.</b>"),
    (">The lesson.</b>", ">Pelajarannya.</b>"),

    # Navigation buttons
    (">Start ↓<", ">Mulai ↓<"),
    (">← Story<", ">← Kisah<"),
    (">← Overview<", ">← Ringkasan<"),
    (">← Samples<", ">← Contoh<"),
    (">Next: ", ">Berikutnya: "),
    (">← Word Agent<", ">← Agen Word<"),
    (">← Excel Agent<", ">← Agen Excel<"),
    (">← PowerPoint Agent<", ">← Agen PowerPoint<"),
    (">← Morning Brief<", ">← Ringkasan Pagi<"),

    # Copy button
    (">Copy</button>", ">Salin</button>"),

    # Story panel headings
    ("Your requirements, mapped", "Kebutuhan Anda, dipetakan"),
    ("The Story", "Kisahnya"),
    ("What is in scope", "Yang termasuk cakupan"),
    ("Sample files", "File contoh"),

    # Lead paragraphs
    ("Short prompts, natural conversation, no framework needed. Perfect for the WhatsApp reply.",
     "Prompt singkat, percakapan natural, tanpa kerangka. Sempurna untuk balasan WhatsApp."),
    ("A single tabular output covering four sections. The four coloured labels below (Goal, Context, Source, Expectation) form the G-C-S-E framework - four labels that turn a vague request into a reliable output.",
     "Satu output tabel yang mencakup empat bagian. Empat label berwarna di bawah (Goal, Context, Source, Expectation) membentuk kerangka G-C-S-E - empat label yang mengubah permintaan samar menjadi output yang dapat diandalkan."),
    ("Open <a href=\"https://m365.cloud.microsoft/chat\" target=\"_blank\">m365.cloud.microsoft/chat</a>. Click the paperclip or drag <code>01 Contoso_Q3_Launch_Memo_Draft.docx</code> into the chat. Type <code>@</code> to open the agent picker, choose <b>Word</b>, then paste:",
     "Buka <a href=\"https://m365.cloud.microsoft/chat\" target=\"_blank\">m365.cloud.microsoft/chat</a>. Klik ikon klip atau seret <code>01 Contoso_Q3_Launch_Memo_Draft.docx</code> ke chat. Ketik <code>@</code> untuk membuka pemilih agen, pilih <b>Word</b>, lalu tempel:"),
    ("The regional marketing team needs the exec summary in Bahasa. Same chat session, next prompt.",
     "Tim marketing regional butuh ringkasan eksekutif dalam Bahasa Indonesia. Sesi chat yang sama, prompt berikutnya."),
    ("The board will read for two minutes and then ask five hard questions. Bu Sari wants to know what they are before the meeting.",
     "Direksi akan membaca selama dua menit lalu mengajukan lima pertanyaan sulit. Bu Sari ingin tahu apa saja sebelum rapat."),
    ("Drag <code>02 Contoso_Admin_Ops_Budget_Q3.xlsx</code> into Copilot Chat. Type <code>@</code> and pick <b>Excel</b>. Paste:",
     "Seret <code>02 Contoso_Admin_Ops_Budget_Q3.xlsx</code> ke Copilot Chat. Ketik <code>@</code> dan pilih <b>Excel</b>. Tempel:"),
    ("Same chat, next prompt. Bu Sari will paste this into the Word memo from Exercise 2.",
     "Chat yang sama, prompt berikutnya. Bu Sari akan menempelkan ini ke memo Word dari Latihan 2."),
    ("Not everything gets escalated. Three items need explanation before the CEO sees them.",
     "Tidak semua perlu dieskalasi. Tiga item butuh penjelasan sebelum CEO melihatnya."),
    ("Drag <code>03 Contoso_Board_Deck_Q3.pptx</code> into Copilot Chat. Type <code>@</code>, choose <b>PowerPoint</b>. Paste:",
     "Seret <code>03 Contoso_Board_Deck_Q3.pptx</code> ke Copilot Chat. Ketik <code>@</code>, pilih <b>PowerPoint</b>. Tempel:"),
    ("BCG and McKinsey call this the \"one-message-per-slide\" style. The title <b>is</b> the conclusion, in a full sentence. The body proves it.",
     "BCG dan McKinsey menyebutnya gaya \"satu pesan per slide\". Judul <b>adalah</b> kesimpulannya, dalam satu kalimat lengkap. Isi slide membuktikannya."),
    ("In case Bu Sari has to open the meeting if the CEO is late.",
     "Untuk berjaga-jaga jika Bu Sari harus membuka rapat saat CEO terlambat."),
    ("Four labels that turn a vague request into a reliable output.",
     "Empat label yang mengubah permintaan samar menjadi output yang dapat diandalkan."),
    ("Enterprise Data Protection (EDP) is what makes free Copilot Chat safe for internal work.",
     "Enterprise Data Protection (EDP) yang membuat Copilot Chat gratis aman untuk pekerjaan internal."),
    ("Everyday admin tasks. Paste, edit the specifics, send.",
     "Tugas admin sehari-hari. Tempel, ubah bagian spesifik, kirim."),

    # Task subheadings h4
    ("<h4>Upload the deck and invoke PowerPoint Agent</h4>",
     "<h4>Unggah deck dan panggil Agen PowerPoint</h4>"),
    ("<h4>Rewrite every slide title as an action title</h4>",
     "<h4>Tulis ulang setiap judul slide sebagai action title</h4>"),
    ("<h4>Speaker notes for every slide</h4>",
     "<h4>Catatan pembicara untuk setiap slide</h4>"),
]

for old, new in R:
    h = h.replace(old, new)

p.write_text(h, encoding="utf-8")
print(f"Written {len(h)} bytes")
