import tkinter as tk
from tkinter import filedialog, messagebox
from pathlib import Path
from pypdf import PdfWriter


def select_pdf_files() -> list[Path]:
    root = tk.Tk()
    root.withdraw()
    files = filedialog.askopenfilenames(
        title="병합할 PDF 파일 선택 (순서대로 선택하세요)",
        filetypes=[("PDF 파일", "*.pdf")],
    )
    root.destroy()
    return [Path(f) for f in files]


def select_output_path() -> Path | None:
    root = tk.Tk()
    root.withdraw()
    path = filedialog.asksaveasfilename(
        title="저장할 파일 이름 입력",
        defaultextension=".pdf",
        filetypes=[("PDF 파일", "*.pdf")],
    )
    root.destroy()
    return Path(path) if path else None


def merge_pdfs(input_paths: list[Path], output_path: Path) -> None:
    writer = PdfWriter()
    for path in input_paths:
        writer.append(str(path))
    with open(output_path, "wb") as f:
        writer.write(f)


def main():
    input_paths = select_pdf_files()
    if len(input_paths) < 2:
        messagebox.showwarning("경고", "PDF 파일을 2개 이상 선택해야 합니다.")
        return

    output_path = select_output_path()
    if not output_path:
        return

    try:
        merge_pdfs(input_paths, output_path)
        messagebox.showinfo("완료", f"병합 완료!\n저장 위치: {output_path}")
    except Exception as e:
        messagebox.showerror("오류", f"병합 중 오류가 발생했습니다:\n{e}")


if __name__ == "__main__":
    main()
