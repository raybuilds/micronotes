import { useState, useEffect } from "react";
 
function App() {
  const [notes, setNotes] = useState([]);
  const [title, setTitle] = useState("");
  const [content, setContent] = useState("");
  const [loading, setLoading] = useState(true);
 
  // TODO 3: on page load, fetch all notes from GET /api/notes
  const fetchNotes = async () => {
    try {
      setLoading(true);
      const response = await fetch("http://localhost:5000/api/notes");
      const data = await response.json();
      setNotes(data);
    } catch (error) {
      console.error("Error fetching notes:", error);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNotes();
  }, []);
 
  // TODO 4: send a POST request with { title, content }, then update the list
  const handleAddNote = async (e) => {
    if (e) e.preventDefault();
    if (!title.trim() || !content.trim()) return;
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

  // DELETE note (Bonus feature)
  const handleDeleteNote = async (id) => {
    try {
      const response = await fetch(`http://localhost:5000/api/notes/${id}`, {
        method: "DELETE",
      });
      if (response.ok) {
        setNotes((prevNotes) => prevNotes.filter((note) => note.id !== id));
      }
    } catch (error) {
      console.error("Error deleting note:", error);
    }
  };
 
  return (
    <div className="container">
      <h1>MicroNotes</h1>
      <form onSubmit={handleAddNote} className="form">
        <input 
          className="input"
          value={title} 
          onChange={(e) => setTitle(e.target.value)} 
          placeholder="Title" 
        />
        <input 
          className="input"
          value={content} 
          onChange={(e) => setContent(e.target.value)} 
          placeholder="Content" 
        />
        <button type="submit" className="btn" disabled={!title.trim()}>
          Add Note
        </button>
      </form>
 
      {loading ? (
        <p className="loading-text">Loading notes...</p>
      ) : (
        <ul className="notes-list">
          {notes.map((note) => (
            <li key={note.id} className="note-item">
              <div className="note-header">
                <h3 className="note-title">{note.title}</h3>
                <button 
                  className="delete-btn" 
                  onClick={() => handleDeleteNote(note.id)}
                  title="Delete Note"
                >
                  Delete
                </button>
              </div>
              <p className="note-content">{note.content}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
}
 
export default App;
