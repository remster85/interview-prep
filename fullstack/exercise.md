# PREREQUISITIES

In order to perform the front-end assessment, you need the following:
- github.com Account
- Frontend development setup needed on a local machine (Visual Studio code is recommended)
- Have ability to push code from local machine to github.com (Have your git environment setup and tested)


# ANGULAR PATH

## Pre-Requisites
- node: 18.x or 20.x (there are LTS versions)  
- npm: 9.x or 10.x
- angular cli ```npm install -g @angular/cli```

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

## REACT PATH

## Pre-Requisites
- node: 16.x, 18.x, or 20.x (there are LTS versions) 
- npm: 7.x or higher

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


# ANGULAR PATH

## Pre-Requisites
- node: 18.x or 20.x (there are LTS versions)  
- npm: 9.x or 10.x  
- angular cli:  
  ```
  npm install -g @angular/cli
  ```

## Part 1 - Initialize the project with a simple form

Create a new app with the following commands:
```
ng new angular-app
cd angular-app
```

Replace `app.component.html`'s content with:
```html
<h2>Test</h2>
```

Edit the component `AppComponent` by importing the FormsModule:
```ts
@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, FormsModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})
```

Serve the application with:
```
ng serve
```

Add the following section to `app.component.html`:
```html
<div>
 <label for="input">Enter text:</label>
 <input id="input" type="text" [(ngModel)]="userInput" />
 <p>You typed: {{ userInput }}</p>
</div>
```

There should be an error.

Amend the file `app.component.ts` to make the solution work and **commit your changes**.

---

## Part 2 - Build the web page to respect the following requirements

The web page is a EUR/USD converter tool. Follow a series of steps you need to code and commit as you go.  
Pay attention to the naming of your variables and your code structure.

### Step 1:

The user should be able to input an amount in EUR and see the converted value in USD.

Add two inputs of type `text` as follows:
- input to accommodate the user’s input in EUR
- input to accommodate the EUR/USD FX rate (for instance it is 1.12)

Add one output of type `text` that displays the converted value in USD.

When entering 1000 EUR and 1.12 as EUR/USD rate, the output should be 1120.

**Commit your changes.**

---

### Step 2:

Let’s allow the user to see the conversion in the way he needs. EUR->USD or USD->EUR.

Add two inputs of type `radio` with the name `inputCurrency`:
- value = EUR
- value = USD

When EUR is selected, the conversion should be done EUR to USD.  
When USD is selected, the conversion should be done USD to EUR.

**Commit your changes.**

---

### Step 3:

The EUR/USD rate will come from an external service but we still let the optionality of the user to override it.

Add a service that will return the FX rate (give the currencyFrom, currencyTo).  
The first implementation of that service returns a hard-coded value of your choice.

To match the need, add an input of type `checkbox` that if selected will allow the user to input the EUR/USD FX value.  
Add the descriptive label next to the input: **"Override the FX rate"**.  
If left to not-selected and consume the FX value from the new service.  
When selected, the override rate should be used.

**Commit your changes.**

---

### Step 4:

To add some dynamism to the application, let’s simulate some activity on the FX rate.  
Let’s suppose the initial value is 1.12 and that every 5 seconds, the value changes by a random value between +0.001 and +0.001.  
Update the application to reflect this behavior.

> 💡 **Hint**:  
> Use a `setInterval` to update the FX rate:
> ```ts
> // Example logic
> const delta = (Math.random() * 0.02) - 0.01; // -0.001 to +0.001
>
> ```

**Angular**:
- Use `setInterval()` in `ngOnInit()` and `clearInterval()` in `ngOnDestroy()`
- Use a flag to prevent updates if FX override is active

**React**:
- Use `useEffect(() => { ... }, [])` to initialize the timer
- Use `setInterval` and `clearInterval` inside the effect
- Use a boolean state flag to skip updates when FX override is enabled

**Commit your changes.**

---

### Step 5:

Now let’s test the validation side of your form.

- When the user input is not a number or is empty, the output should be hidden and an error message should be displayed.
- When the FX rate is invalid, the output should also be hidden and a second error message should be displayed.
- Ensure the user knows whether they are converting EUR->USD or USD->EUR.

**Commit your changes.**

---

### Step 6:

Let’s add a bit of styling to make the app more readable.

- Organize the input fields with titles and spacing.
- Display the result using a border or box layout.
- Error messages should be in red and easy to read.

Use only basic CSS (no third-party libraries).

**Commit your changes.**

---

### Step 7:

Make sure the app is **mobile friendly**.

- Use CSS media queries or flex layout to allow the form and result to adjust to a small screen (mobile or tablet).
- Check alignment, spacing, and responsiveness.

**Commit your changes.**

### Step 8: Keep a History of Conversions

Every time the user enters a valid amount and FX rate, store the result in a **conversion history**.

- Maintain an array of the last **5 conversions**.
- Display the history in a **table format** with the following columns:
  - Timestamp (local time)
  - Input Currency
  - Input Amount
  - FX Rate
  - Converted Amount

Only show the table if there is at least one entry.

**Angular**: Store the history in a component variable and update it inside the conversion method. Use `*ngIf` to conditionally render the table.

**React**: Use `useState` to store the history and `useEffect` if needed to manage side effects. Render the table conditionally.

**Commit your changes.**

---

### Step 9: Add a Reset Button

Add a button labeled **"Reset"** that clears:
- The input amount
- The FX rate (if override is selected)
- The output value
- Any error messages
- The conversion history

This allows the user to start fresh without refreshing the browser.

**Angular**: Create a `reset()` method and bind it to the button’s `(click)` event.

**React**: Define a `handleReset()` function and bind it to the button's `onClick` handler.

**Commit your changes.**

---

### Step 10: Add a Clipboard Copy Feature

Next to the result field, add a button that lets the user **copy the converted value** to the clipboard.

- When clicked, it should show a tooltip or short message like “Copied!” for a brief moment.
- This is useful for UX and demonstrates use of native browser APIs.

**Angular**: Use `navigator.clipboard.writeText()` in a click handler. Use a boolean flag to show the message for a few seconds.

**React**: Use `navigator.clipboard.writeText()` inside the `onClick` handler. Use `useState` and `setTimeout` to toggle the "Copied!" message.

**Commit your changes.**

---

### Step 11: Add a Unit Test

Create at least one **unit test** that checks the core conversion logic:
- Given an amount and an FX rate, the function returns the correct converted value.
- Test both EUR → USD and USD → EUR directions.

**Angular**: Use Jasmine + Karma and test a conversion utility function or service.

**React**: Use Jest and test the conversion function in isolation.

**Commit your changes.**

---

### Step 12: Add a Service Error Simulation

Add a button labeled **"Simulate FX Service Failure"**.

- When clicked, the FX rate service should return an error instead of a value.
- Your app should:
  - Show an error message like "Unable to fetch FX rate."
  - Prevent conversion from taking place.
- Add a second button to **"Restore Service"** and return the app to normal behavior.

**Angular**: Use a flag in the component to toggle service behavior and display the error using conditional rendering.

**React**: Use a state variable to simulate the failure and use conditional rendering for the error message.

**Commit your changes.**



   
