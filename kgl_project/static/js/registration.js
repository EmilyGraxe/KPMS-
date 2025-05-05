
window.onload = function() {
    if ('credentials' in navigator) {
        navigator.credentials.preventSilentAccess && navigator.credentials.preventSilentAccess();
    }};
  //display time
     function updateTime() {
      const now = new Date();
      const timeString = now.toLocaleTimeString();
      document.getElementById('current-time').textContent = ` ${timeString}`;
  }
  setInterval(updateTime, 1000); // Update every second
  updateTime(); // Initial call to display time immediately

  let index = 0;
  const slides = document.getElementsByClassName('slide');
  const produceName = document.getElementById('produce-name');
  function showSlide () {
      for (let i = 0; i < slides.length; i++) {
          slides[i].style.display = 'none';
      }
      slides[index].style.display = 'block';
      const name = slides[index].getAttribute('data-name');
      produceName.textContent = name;
      index = (index + 1) % slides.length;
  }
  showSlide(); // Show the first slide immediately
  setInterval(showSlide, 3000); // Change slide every 3 seconds
  

const alphaNumericKeys = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.split('');
const specialChars = ['@', '#', '$', '&', '_', '.', '-', '*'];
const keyboard = document.getElementById('keyboard');
const inputField = document.getElementById('user_input');

let shiftActive = false; // Initialize shift state
let allbuttons = []; // Array to store all buttons

const allKeys = [...alphaNumericKeys, ...specialChars];


allKeys.forEach(char => {
  const button = document.createElement('button');
  button.innerText = char;
  button.style.color = 'black'; // Change text color to black
  button.style.fontWeight = 'bold'; // Make text bold
  button.onclick = (e) => {
    e.preventDefault();
    let inputChar = shiftActive ? char.toLowerCase() : char; // Check shift state

    inputField.value += inputChar; // Append character to input field
  };
  allbuttons.push(button); // Store button in array
  
  keyboard.appendChild(button);
});

 //create shift button
 const shiftBtn = document.createElement('button');
 shiftBtn.innerText = 'SHIFT'; 
 shiftBtn.classList.add('wide-key');
 shiftBtn.style.gridColumn = 'span 2'; // Make it span two columns
 shiftBtn.style.backgroundColor = 'darkgreen'; // Change background color to green
 shiftBtn.style.color = 'white'; // Change text color to white
 shiftBtn.onclick = (e) => {
   e.preventDefault();
   shiftActive = !shiftActive; // Toggle shift state
   // Update button text based on shift state
   allbuttons.forEach(btn => {
      if (shiftActive) {
        btn.innerText = btn.innerText.toLowerCase(); // Change to lowercase
      } else {
        btn.innerText = btn.innerText.toUpperCase();
        btn.backgroundColor = 'lightblue'; // Change to uppercase
      }
    });
   
 };
     
  keyboard.appendChild(shiftBtn); // Append shift button to keyboard
     

const delBtn = document.createElement('button');
delBtn.innerText = 'Undo';
delBtn.classList.add('wide-key');
delBtn.style.gridColumn = 'span 2'; // Make it span two columns
delBtn.style.backgroundColor = 'darkorange'; // Change background color to orange
delBtn.style.color = 'white'; // Change text color to white
delBtn.onclick = (e) => {
  e.preventDefault();
  inputField.value = inputField.value.slice(0, -1);
};
keyboard.appendChild(delBtn);

const clearBtn = document.createElement('button');
clearBtn.innerText = 'Clear';
clearBtn.classList.add('wide-key');
clearBtn.style.gridColumn = 'span 2'; // Make it span two columns
clearBtn.style.backgroundColor = 'darkred'; // Change background color to red
clearBtn.style.color = 'white'; // Change text color to white
clearBtn.onclick = (e) => {
  e.preventDefault();
  inputField.value = '';
};
keyboard.appendChild(clearBtn);



