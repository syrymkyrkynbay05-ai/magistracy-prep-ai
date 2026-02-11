from fpdf import FPDF
import os


class MagisCoreProposal(FPDF):
    def header(self):
        if self.page_no() > 1:
            # Small logo in header for other pages
            logo_path = os.path.join(os.getcwd(), "public", "logo no bg, blue.png")
            if os.path.exists(logo_path):
                self.image(logo_path, 10, 8, 10)

            self.set_font("CustomArial", "", 8)
            self.set_text_color(128, 128, 128)
            self.cell(0, 10, "MagisCore — SiteQur компаниясының шешімі", 0, 0, "R")
            self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font("CustomArial", "", 8)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f"Бет {self.page_no()} | SiteQur © 2026", 0, 0, "C")


def create_proposal():
    pdf = MagisCoreProposal()

    # Get Windows Font Path
    windir = os.environ.get("WINDIR", "C:\\Windows")
    font_path = os.path.join(windir, "Fonts", "arial.ttf")
    font_bold_path = os.path.join(windir, "Fonts", "arialbd.ttf")

    if not os.path.exists(font_path):
        return

    pdf.add_font("CustomArial", "", font_path)
    pdf.add_font("CustomArialB", "", font_bold_path)

    pdf.add_page()

    # --- Title Page ---
    # Logo
    logo_path = os.path.join(os.getcwd(), "public", "logo no bg, blue.png")
    if os.path.exists(logo_path):
        pdf.image(logo_path, x=85, y=40, w=40)

    pdf.ln(80)
    pdf.set_font("CustomArialB", "", 28)
    pdf.set_text_color(22, 53, 92)  # Dark Blue
    pdf.cell(0, 20, "MagisCore", 0, 1, "C")

    pdf.set_font("CustomArialB", "", 16)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, "Инновациялық білім беру платформасы", 0, 1, "C")

    pdf.ln(30)
    pdf.set_font("CustomArial", "", 14)
    pdf.cell(0, 10, "Автор: Азамат Пердеев", 0, 1, "C")
    pdf.set_font("CustomArialB", "", 14)
    pdf.cell(0, 10, "Компания: SiteQur", 0, 1, "C")

    pdf.ln(50)
    pdf.set_font("CustomArial", "", 11)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 10, "Коммерциялық ұсыныс | 2026 жыл", 0, 1, "C")

    # Page 2: Problem & Context
    pdf.add_page()
    pdf.set_font("CustomArialB", "", 18)
    pdf.set_text_color(22, 53, 92)
    pdf.cell(0, 15, "1. Нарықтағы мәселелер мен қажеттіліктер", 0, 1, "L")

    pdf.set_font("CustomArial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(
        0,
        10,
        (
            "Магистратураға дайындық — бұл жоғары жауапкершілікті талап ететін процесс. "
            "Алайда, қазіргі оқу орталықтары мынадай «тар» жерлерге тап болуда:\n\n"
            "• Контенттің ескіруі: Динамикалық түрде өзгермейтін тест базалары.\n"
            "• Аналитиканың жоқтығы: Студенттің қай тақырыптан ақсап тұрғанын білмеу.\n"
            "• Шығындардың көптігі: Тесттерді басып шығару және адам күшімен тексеру.\n"
            "• Масштабталу шектеуі: Оқушы саны артқан сайын бақылаудың қиындауы."
        ),
    )

    # Page 3: Our Solution
    pdf.ln(10)
    pdf.set_font("CustomArialB", "", 18)
    pdf.set_text_color(22, 53, 92)
    pdf.cell(0, 15, "2. MagisCore — SiteQur-дан заманауи шешім", 0, 1, "L")

    pdf.set_font("CustomArial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(
        0,
        10,
        (
            "MagisCore — бұл SiteQur компаниясының білім беруді цифрландыру бағытындағы флагмандық жобасы.\n\n"
            "Платформаның артықшылықтары:\n"
            "• Smart Content: 800-ден астам өзекті сұрақ (Gemini AI көмегімен жаңартылған).\n"
            "• Ресми формат: Listening, Reading және профильдік пәндердің толық циклі.\n"
            "• AI Көмекші: Сұрақтарды жай ғана белгілемей, олардың қисынын түсіндіру.\n"
            "• Анти-чит: Академиялық адалдықты сақтайтын техникалық қорғаныс қабаттары."
        ),
    )

    # Page 4: Business Value
    pdf.add_page()
    pdf.set_font("CustomArialB", "", 18)
    pdf.set_text_color(22, 53, 92)
    pdf.cell(0, 15, "3. Бизнестің өсуіне әсері", 0, 1, "L")

    pdf.set_font("CustomArial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(
        0,
        10,
        (
            "SiteQur ұсынған MagisCore жүйесі компанияңызға келесі мүмкіндіктерді береді:\n\n"
            "1. Тиімділік (Efficiency): Оқытушылардың уақытын 40%-ға үнемдеу.\n"
            "2. Сапа (Quality Control): Білім деңгейін ешқандай қатесіз, автоматты бағалау.\n"
            "3. Көшбасшылық: Нарықта бірінші болып AI технологияларын енгізу.\n"
            "4. Деректер: Әр оқушының прогресі бойынша нақты деректерге негізделген шешім қабылдау."
        ),
    )

    # Page 5: Conclusion
    pdf.ln(15)
    pdf.set_font("CustomArialB", "", 18)
    pdf.set_text_color(22, 53, 92)
    pdf.cell(0, 15, "4. Ынтымақтастыққа шақыру", 0, 1, "L")

    pdf.set_font("CustomArial", "", 12)
    pdf.set_text_color(0, 0, 0)
    pdf.multi_cell(
        0,
        10,
        (
            "Біз SiteQur ретінде сіздің орталықтың білім сапасын жаңа деңгейге шығаруға дайынбыз. "
            "MagisCore — бұл инвестиция, ол өзін қысқа мерзімде сапалы нәтижемен ақтайды."
        ),
    )

    pdf.ln(30)
    pdf.set_font("CustomArialB", "", 12)
    pdf.cell(0, 8, "Азамат Пердеев", 0, 1, "L")
    pdf.set_font("CustomArial", "", 11)
    pdf.cell(0, 8, "Негізін қалаушы, SiteQur", 0, 1, "L")
    pdf.set_text_color(22, 53, 92)
    pdf.cell(0, 8, "sitequr.kz | MagisCore Team", 0, 1, "L")

    output_path = os.path.join(os.getcwd(), "MagisCore_Business_Proposal.pdf")
    pdf.output(output_path)
    print(f"PDF created at: {output_path}")


if __name__ == "__main__":
    create_proposal()
