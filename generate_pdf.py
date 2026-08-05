import os
from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        # Only show header on pages after the cover / first page if needed, 
        # but here we keep it clean.
        pass

    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        self.set_font("helvetica", "I", 9)
        # Page number
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

def create_report_pdf():
    pdf = PDFReport()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Title
    pdf.set_font("helvetica", "B", 22)
    pdf.cell(0, 12, "MicroNotes Project Report", ln=True, align="C")
    pdf.ln(4)
    
    # Metadata Box
    pdf.set_font("helvetica", "B", 10)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(0, 5, "Author: raybuilds", ln=True, align="C")
    pdf.cell(0, 5, "Date: August 5, 2026", ln=True, align="C")
    pdf.cell(0, 5, "Assignment: Build MicroNotes App", ln=True, align="C")
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)
    
    # Horizontal line
    pdf.line(10, pdf.get_y(), 200, pdf.get_y())
    pdf.ln(6)
    
    # Section 1
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "1. What is the Difference Between Frontend and Backend?", ln=True)
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10.5)
    frontend_backend_text = (
        "The frontend is the client-side of the application that runs directly in the user's browser, "
        "responsible for rendering the User Interface (UI), capturing user actions, and managing local "
        "component state (built using HTML, CSS, and React in this app). In contrast, the backend is the "
        "server-side that runs on a remote host (built with Node.js and Express here), handling business "
        "logic, authentication, and hosting the data store. While the frontend presents information visually "
        "and provides a user-friendly layout, the backend serves as the single source of truth that "
        "processes API requests, performs calculations, and decides what data to send back. They "
        "communicate over the network using standard protocols like HTTP via structured REST endpoints."
    )
    pdf.multi_cell(0, 6, frontend_backend_text)
    pdf.ln(8)
    
    # Section 2
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "2. What Does async/await Actually Do?", ln=True)
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10.5)
    async_await_text = (
        "In JavaScript, asynchronous code is used to perform operations that take time (such as fetching "
        "data from a server) without freezing the entire browser interface. A Promise represents a value "
        "that will become available in the future.\n\n"
        "The async/await syntax is a clean, readable way to work with these Promises. By marking a function "
        "as async, we are allowed to use the await keyword inside it. The await keyword pauses the execution "
        "of that specific function until the Promise resolves, returning the actual result directly. "
        "This avoids nesting multiple callback blocks (often referred to as 'callback hell') and keeps "
        "the codebase highly maintainable."
    )
    pdf.multi_cell(0, 6, async_await_text)
    pdf.ln(4)
    
    # Code block
    pdf.set_font("helvetica", "B", 10)
    pdf.cell(0, 5, "Example implementation from App.jsx:", ln=True)
    pdf.ln(1)
    
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("courier", "", 9)
    code_text = (
        "const fetchNotes = async () => {\n"
        "  try {\n"
        "    setLoading(true);\n"
        "    // 1. Await pauses here until the network request completes and returns the response\n"
        "    const response = await fetch(\"http://localhost:5000/api/notes\");\n"
        "    // 2. Await pauses here until the response body is parsed into JSON\n"
        "    const data = await response.json();\n"
        "    setNotes(data);\n"
        "  } catch (error) {\n"
        "    console.error(\"Error fetching notes:\", error);\n"
        "  } finally {\n"
        "    setLoading(false);\n"
        "  }\n"
        "};"
    )
    pdf.multi_cell(0, 5, code_text, fill=True, border=1)
    pdf.ln(8)
    
    # Add new page for screenshot and Section 4 to avoid awkward page breaks
    pdf.add_page()
    
    # Section 3: App Screenshot
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "3. App Screenshot (Showing 2 Notes)", ln=True)
    pdf.ln(2)
    
    screenshot_path = "screenshot.png"
    if os.path.exists(screenshot_path):
        # Insert image (centered, width 160mm)
        pdf.image(screenshot_path, x=25, w=160)
        pdf.ln(4)
    else:
        pdf.set_font("helvetica", "I", 10)
        pdf.cell(0, 6, "[Screenshot image 'screenshot.png' not found in project directory]", ln=True)
        pdf.ln(4)
        
    pdf.ln(6)
    
    # Section 4
    pdf.set_font("helvetica", "B", 14)
    pdf.cell(0, 8, "4. One Thing That Was Confusing and How I Figured It Out", ln=True)
    pdf.ln(2)
    pdf.set_font("helvetica", "", 10.5)
    confusing_text = (
        "A particularly confusing issue occurred when trying to push the project commits to the remote "
        "GitHub repository. Git rejected the push command with a 403 Forbidden error stating that permission "
        "was denied to a previously cached account ('va7tech-coder').\n\n"
        "How it was resolved:\n"
        "1. Checked Git settings using 'git config --local --get-regexp user' and confirmed the local repository "
        "details were correct, but the system credentials manager was still injecting the wrong account token.\n"
        "2. Generated a Personal Access Token (PAT) with full 'repo' access scopes from the 'raybuilds' GitHub account.\n"
        "3. Updated the Git remote origin URL to include the token: 'git remote set-url origin https://<PAT_TOKEN>@github.com/raybuilds/micronotes.git'.\n"
        "4. Executed the push again, which successfully verified writing credentials. This highlighted the "
        "distinction between Git author commit metadata and network push authorization credentials."
    )
    pdf.multi_cell(0, 6, confusing_text)
    
    # Save output
    pdf.output("report.pdf")
    print("report.pdf successfully generated!")

if __name__ == "__main__":
    create_report_pdf()
