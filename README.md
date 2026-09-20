# Phase — Python Obfuscator

---

## 🌐 Select your language

| Language / Ngôn ngữ | Link |
|---|---|
| English | [English README](#-english) |
| Tiếng Việt | [Vietnamise README](#-tiếng-việt) |

---

# 🇬🇧 English

Phase is a Python obfuscator that turns a readable script into a deeply obfuscated, self-protecting blob. It buries your code inside a custom bytecode VM and a multi-layer encrypted payload that refuses to run if it's tampered with, debugged, or hooked.

> Author: KTN (Trương Nhật Bảo Nam) — Repo: github.com/ktn1703/Phase-Obfuscator

## What it does

The pipeline roughly is: clean the source → rename every variable → hide strings and ints behind XOR/MBA expressions → inject junk code → flatten the control flow into a state machine → lift the whole thing into a custom BVM bytecode → encrypt it through 5 nested layers → glue it behind anti-debug and anti-hook guards.

### Key features

- **BVM Engine** — the code is rebuilt into a custom bytecode format. Traditional decompilers are useless against it.
- **5-layer crypto** — Shuffle → XOR → ChaCha20 → AES-256-GCM → zlib, each layer with its own key (HKDF-SHA256).
- **String & int obfuscation** — multiple XOR schemes for strings, MBA expressions for ints. Nothing stays in plaintext.
- **Variable renaming** — every name becomes a mix of confusable characters (`I`, `l`, `1`, `O`, `0`).
- **Junk code injection** — 14–22 dead functions with opaque predicates to add noise.
- **Control flow flattening** — linear logic turns into a state-machine loop.
- **Anti-everything** — anti-debug, anti-hook, anti-frame, anti-VM, anti-proxy, anti-decompiler (makes `pycdc` choke), anti-crack request.
- **Tamper-proof** — the payload verifies the SHA-256 of its own file; changing a single byte means self-destruct. If it detects it's being inspected, it burns CPU and calls `TerminateProcess`.
- **Optional** — `--hw-bind` locks execution to hardware, `--py-lock` locks it to a Python version.

## Usage

### Command line

```bash
python aevanish.py -f input.py -o output.py
```

Or just run `python aevanish.py` for interactive mode.

| Flag | Meaning |
|---|---|
| `-f, --file` | Script to obfuscate |
| `-o, --output` | Output file (default: `input_obf.py`) |
| `--no-anti-debug` | Disable anti-debug |
| `--no-anti-hook` | Disable anti-hook |
| `--no-anti-frame` | Disable anti-frame / stack inspection |
| `--no-junk` | Disable junk code injection |
| `--no-anti-vm` | Disable VM/sandbox detection |
| `--no-anti-proxy` | Disable anti-MITM/proxy |
| `--no-anti-pydc` | Disable anti-decompiler |
| `--no-anti-crack` | Disable network-request blocking |
| `--hw-bind` | Lock to current hardware |
| `--py-lock` | Lock to current Python version |
| `--silent` | No output |
| `--banner` | Show banner |

### Examples

```bash
# Quick run, all protections on
python aevanish.py -f bot.py

# Custom output name
python aevanish.py -f bot.py -o secured.py

# Hardware lock
python aevanish.py -f bot.py -o secured.py --hw-bind

# Light pass to debug your own script
python aevanish.py -f tool.py --no-anti-debug --no-junk
```

### Interactive mode

Run `python aevanish.py` with no arguments and follow the prompts. Drop your file in, answer the questions, done.

## Notes

- Requires **Python 3.8+**, zero dependencies. Output runs standalone.
- Obfuscation makes code hard to reverse, not impossible — always keep the original source safe.
- For educational and authorized security research purposes only.

---

# 🇻🇳 Tiếng Việt

Phase là tool obfuscate Python code của mình. Nó biến một file script đọc được bình thường thành một khối code xào nát, tự bảo vệ và chống đủ thứ chống — từ decompiler, debugger cho tới hooking và detect máy ảo.

> Tác giả: KTN (Trương Nhật Bảo Nam) — Repo: github.com/ktn1703/Phase-Obfuscator

## Nó làm gì

Pipeline đại khái: dọn source → đổi tên biến → mã hóa string dạng XOR → biến số nguyên thành biểu thức MBA → bơm junk code → nén control flow thành state-machine → compile nguyên cục sang BVM format → bọc 5 lớp mã hóa → dán lên đầu một loader chống soi.

### Tính năng chính

- **BVM Engine** — code được dựng lại thành format bytecode custom. Decompiler truyền thống vô dụng.
- **5 lớp mã hóa** — Shuffle → XOR → ChaCha20 → AES-256-GCM → zlib, mỗi lớp một key riêng (HKDF-SHA256).
- **Mã hóa string & số** — đủ loại XOR schemes cho string, MBA cho số. Không gì nằm ở plaintext.
- **Đổi tên biến** — biến hết thành mớ ký tự dễ nhầm (`I`, `l`, `1`, `O`, `0`).
- **Junk code** — nhét 14–22 hàm "chết" với opaque predicates cho thêm loạn.
- **Control flow flattening** — logic thẳng chuyển thành vòng lặp state-machine.
- **Chống đủ thứ** — anti-debug, anti-hook, anti-frame, anti-VM, anti-proxy, anti-decompiler (làm `pycdc` chết ngay), anti-crack request.
- **Chống sửa file** — payload kiểm tra SHA-256 của chính mình, đụng 1 byte là tự hủy. Bị soi là burn CPU + `TerminateProcess`.
- **Tùy chọn** — `--hw-bind` khóa theo phần cứng, `--py-lock` khóa theo phiên bản Python.

## Cách dùng

### Command line

```bash
python aevanish.py -f input.py -o output.py
```

Hoặc chỉ gõ `python aevanish.py` để chạy interactive.

| Cờ | Ý nghĩa |
|---|---|
| `-f, --file` | File script cần obfuscate |
| `-o, --output` | File output (mặc định: `input_obf.py`) |
| `--no-anti-debug` | Tắt chống debug |
| `--no-anti-hook` | Tắt chống hook |
| `--no-anti-frame` | Tắt chống frame / stack |
| `--no-junk` | Tắt junk code |
| `--no-anti-vm` | Tắt detect máy ảo |
| `--no-anti-proxy` | Tắt chống MITM/proxy |
| `--no-anti-pydc` | Tắt anti-decompiler |
| `--no-anti-crack` | Tắt chặn network request |
| `--hw-bind` | Khóa chạy theo hardware |
| `--py-lock` | Khóa theo Python version hiện tại |
| `--silent` | Không in gì ra |
| `--banner` | Hiện banner |

### Ví dụ

```bash
# Chạy nhanh, bật hết protection
python aevanish.py -f bot.py

# Đổi tên file output
python aevanish.py -f bot.py -o secured.py

# Khóa theo phần cứng
python aevanish.py -f bot.py -o secured.py --hw-bind

# Obfuscate nhẹ để debug lại script của mình
python aevanish.py -f tool.py --no-anti-debug --no-junk
```

### Chế độ tương tác

Chạy `python aevanish.py` không tham số, nó sẽ hướng dẫn từng bước. Kéo file vào, trả lời mấy câu hỏi là xong.

## Ghi chú

- Cần **Python 3.8+**, không cần dependency gì. File output chạy độc lập.
- Obfuscation làm code khó reverse, không phải bất khả xâm phạm — luôn giữ source gốc cẩn thận.
- Chỉ dùng cho mục đích học tập và bảo mật hợp pháp.
