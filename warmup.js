// Part A — JavaScript Warm-Up

console.log("--- A1. Variables & Data Types ---");
{
  const title = "My First Note";
  const isPinned = false;
  const tags = ["personal", "todo"];
 
  console.log(title, typeof title);
  console.log(isPinned, typeof isPinned);
  console.log(tags, typeof tags);
}

console.log("\n--- A2. A Simple Function ---");
{
  const makeNote = (title, content) => {
    return { title, content, createdAt: new Date() };
  };
 
  console.log(makeNote("Groceries", "Milk, eggs, bread"));
}

console.log("\n--- A3. Arrays: Loop Through Notes ---");
let notes = [];
{
  notes = [
    { title: "Groceries", content: "Milk, eggs" },
    { title: "Workout", content: "Legs day" },
    { title: "Reading", content: "Finish chapter 3" },
  ];
 
  const titles = notes.map(note => note.title);
  console.log(titles);
}

console.log("\n--- A4. Destructuring & Template Literals ---");
{
  const { title, content } = notes[0];
  console.log(`${title}: ${content}`);
}

console.log("\n--- A5. Async/Await Basics ---");
{
  async function getSampleData() {
    const response = await fetch("https://jsonplaceholder.typicode.com/todos/1");
    const data = await response.json();
    console.log(data);
  }
 
  getSampleData();
}
