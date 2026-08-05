import { useState, useEffect } from "react";
 
function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
 
  // TODO 3: on page load, fetch all notes from GET /api/notes
  // hint: use useEffect + async/await, same pattern as warmup.js A5
  const fetchNotes = async () => {
    try {
      const response = await fetch("http://localhost:5000/api/notes");
      const data = await response.json();
      setNotes(data);
    } catch (error) {
      console.error("Error fetching notes:", error);
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);
 
  // TODO 4: send a POST request with { title, content }, then update the list
  const handleAddNote = async () => {
    if (!title || !content) return;
    try {
      const response = await fetch("http://localhost:5000/api/notes", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ title, content }),
      });
      if (response.status === 201) {
        const newNote = await response.json();
        setNotes((prevNotes) => [...prevNotes, newNote]);
        setTitle("");
        setContent("");
      }
    } catch (error) {
      console.error("Error adding note:", error);
    }
  };
 
  return (
    <div>
      <h1>MicroNotes</h1>
      <input value={title} onChange={(e) => setTitle(e.target.value)} placeholder="Title" />
      <input value={content} onChange={(e) => setContent(e.target.value)} placeholder="Content" />
      <button onClick={handleAddNote}>Add Note</button>
 
      <ul>
        {notes.map((note) => (
          <li key={note.id}>{note.title}: {note.content}</li>
        ))}
      </ul>
    </div>
  );
}
 
export default App;
