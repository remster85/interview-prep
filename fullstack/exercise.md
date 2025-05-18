# ANGULAR

npm install -g @angular/cli

## Part 1 - Initialize the project with a simple form
Create a new app with following commands:

```
ng new angular-app
cd angular-app
```

Replace app.component.html 's content  with ```<h2>Test</h2>```.  
Edit the component Appcomponent by importing the FormsModule.
```
@Component({
  selector: 'app-root',
  imports: [RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
```
Serve the application with command ng serve, it should work.

Add the following section to app.component.html
```
<div>
 <label for="input">Enter text:</label>
 <input id="input" type="text" [(ngModel)]="userInput" />
<p>You typed: {{ userInput }}</p>
</div>
```

There should be an error.

Amend the file app.component.ts to make the solution works and Commit your changes.

## REACT

## Part 1 - Initialize the project with a simple form
Create a new app with following commands:

```
npx create-react-app react-app
cd react-app
npm start
```

The application should work.  


Replace App.js content with:
```
import './App.css';

function App() {
  return (
    <div>
      <h2>Test</h2>
      <div>
        <label htmlFor="input">Enter text:</label>
        <input
          id="input"
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
        />
        <p>You typed: {userInput}</p>
      </div>
    </div>
  );
}
export default App;
```

There should be an error.

Amend the file App.js to make the solution works and Commit your changes.


### Part 2- Build the web page to respect the following requirements





   
