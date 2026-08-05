# MicroNotes Project Report

**Author:** raybuilds  
**Date:** August 5, 2026  
**Assignment:** Build MicroNotes App  

---

## 1. What is the Difference Between Frontend and Backend?

The frontend is the client-side of the application that runs directly in the user's browser, responsible for rendering the User Interface (UI), capturing user actions, and managing local component state (built using HTML, CSS, and React in this app). In contrast, the backend is the server-side that runs on a remote host (built with Node.js and Express here), handling business logic, authentication, and hosting the data store. While the frontend presents information visually and provides a user-friendly layout, the backend serves as the single source of truth that processes API requests, performs calculations, and decides what data to send back. They communicate over the network using standard protocols like HTTP via structured REST endpoints.

---

## 2. What Does `async/await` Actually Do?

In JavaScript, asynchronous code is used to perform operations that take time (such as fetching data from a server) without freezing the entire browser interface. A `Promise` represents a value that will become available in the future.

The `async/await` syntax is a clean, readable way to work with these Promises. By marking a function as `async`, we are allowed to use the `await` keyword inside it. The `await` keyword pauses the execution of that specific function until the Promise resolves, returning the actual result directly.

### Example from `App.jsx` (`TODO 3`):
```javascript
const fetchNotes = async () => {
  try {
    setLoading(true);
    // 1. Await pauses here until the network request completes and returns the response
    const response = await fetch("http://localhost:5000/api/notes");
    // 2. Await pauses here until the response body is parsed into JSON
    const data = await response.json();
    setNotes(data);
  } catch (error) {
    console.error("Error fetching notes:", error);
  } finally {
    setLoading(false);
  }
};
```
Without `async/await`, we would have to chain callbacks using `.then()` blocks (e.g., `fetch().then(r => r.json()).then(data => ...)`), which quickly makes the code harder to read and debug. `async/await` lets asynchronous code read sequentially, like traditional synchronous code, while maintaining non-blocking performance.

---

## 3. App Screenshot

*Insert your screenshot of the running application here, showing at least 2 notes in the list.*

![MicroNotes Screenshot](screenshot.png)

---

## 4. One Thing That Was Confusing and How I Figured It Out

A particularly confusing issue occurred when trying to push the project commits to the remote GitHub repository. Git rejected the push command with a `403 Forbidden` error:
`remote: Permission to raybuilds/micronotes.git denied to va7tech-coder.`

**How it was figured out:**
1. I checked the current Git credentials using `git config --local --get-regexp user` and realized that while I configured the project's local config to use `raybuilds` as the author name, the underlying system (Windows Credential Manager) was still passing stored credentials for a different account (`va7tech-coder`).
2. To resolve this, we generated a Personal Access Token (PAT) with `repo` scopes from the `raybuilds` GitHub account.
3. We then updated the Git remote URL to embed the token:
   `git remote set-url origin https://<PAT_TOKEN>@github.com/raybuilds/micronotes.git`
4. Running `git push origin main` again succeeded immediately since the embedded token bypassed the Credential Manager's cached credentials. This taught me the important difference between Git commit author configuration and the actual credentials used for server-side HTTP/HTTPS authentication.
