// for the home page
window.addEventListener('scroll', function () {
    const navbar = document.getElementById('navbar');
    if (window.scrollY > 50) {
      navbar.classList.remove('bg-emerald-700');
      navbar.classList.add('bg-emerald-900');
    } else {
      navbar.classList.add('bg-emerald-700');
      navbar.classList.remove('bg-emerald-900');
    }
  });

  const myAccountDropdownToggle = document.getElementById('myAccountDropdownToggle');
  const myAccountDropdown = document.getElementById('myAccountDropdown');
  const dropdownIcon = document.getElementById('dropdownIcon');

  if (myAccountDropdownToggle) {
  myAccountDropdownToggle.addEventListener('click', function (event) {
      event.preventDefault();
      myAccountDropdown.classList.toggle('hidden');
      dropdownIcon.classList.toggle('ri-arrow-down-s-line');
      dropdownIcon.classList.toggle('ri-arrow-up-s-line');
  });

  document.addEventListener('click', function (event) {
      if (!myAccountDropdown.contains(event.target) && !myAccountDropdownToggle.contains(event.target)) {
      myAccountDropdown.classList.add('hidden');
      dropdownIcon.classList.add('ri-arrow-down-s-line');
      dropdownIcon.classList.remove('ri-arrow-up-s-line');
      }
  });
  }

  //comuting total nights
  const countNights = (checkin, checkout) => {
    const total = document.getElementById('night-total')
    const totalMobile = document.getElementById('night-total-mobile')

    checkinSplit = checkin.split('-')
    checkoutSplit = checkout.split('-')
    const totalNights = parseInt(checkoutSplit[1]) - parseInt(checkinSplit[1]) 
    total.textContent = totalNights
    totalMobile.textContent = totalNights
  }


  // Booking Form Submission with URL Parameters
  // let activeField = null;
  let checkInInput;
  let checkOutInput;
  let minCheckoutDate = document.getElementById('checkin-date');

  // Setup Flatpickr for Check In
  flatpickr("#checkinInput", {
  dateFormat: "m-d-Y",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      checkInDate.value = dateStr;
      minCheckoutDate = dateStr;
      }
  }
  });

  // Setup Flatpickr for Check Out
  flatpickr("#checkoutInput", {
  dateFormat: "m-d-Y",
  minDate:`${minCheckoutDate.innerText}`,
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      checkOutInput.value = dateStr;
      
      // activeField = "checkoutInput";
      // document.getElementById("modalTime").value = "";
      // document.getElementById("timePickerModal").classList.remove("hidden");
      // document.getElementById("modalTitle").textContent = `Select Time for ${dateStr}`;
      }
  }
  });

  //get the price elemetn
  const priceElem = document.getElementById('total-price')
  const priceElemMobile = document.getElementById('total-price-mobile')
  let totalPrice = 0
  const computeRoomPrice = (basePrice, qty) => {
    const total = basePrice * qty
    totalPrice += total
  }
  
  //Room Tracking Code
  const displayRooms = document.getElementById('display-rooms')
  let room = {}

  //Add event listeners to all dropdowns
  const roomDropDowns = document.querySelectorAll('#select-room-dropdown')
  const roomTypeNames = document.querySelectorAll('#room-name') //get all of the room name
  const roomPrices = document.querySelectorAll('#room-price')
  
  let count = 0 //for accessing the room type nodelist. SEE: roomTypeIds 
  roomDropDowns.forEach(dropdown => {
      const roomName =  roomTypeNames[count].outerText //retrieve the text value from the nodelist
      const roomPrice = roomPrices[count].outerText
      
      dropdown.addEventListener('change', function() {     
          room[roomName] = {num: this.value, price:roomPrice} //Data selected by the customer. Actual data structure     

          

          //CASE: Deleted the old content
            if (displayRooms.innerText !== '') {
              displayRooms.innerHTML = "";
            }
            
          for (key in room) {
            if(room[key].num === '0') {
              delete room[key]
              console.log('deleted')
            }
            
            //for display
            //assign new value
            const newPara = document.createElement('span')
            newPara.classList = "text-xs"
            //Outputs the newest data
            newPara.innerText = `${room[key].num}x ${key}`
            displayRooms.appendChild(newPara)
          }
          //Compute first and update the total
          computeRoomPrice(roomPrice, this.value)
          priceElem.innerText = parseFloat(totalPrice)
          priceElemMobile.innerText = parseFloat(totalPrice)
          console.log(room)
      })

      count += 1
  })
  
  






  // Confirm time selection
// Confirm time selection
// document.getElementById("modalConfirm").addEventListener("click", () => {
//     const time = document.getElementById("modalTime").value;
//     if (!time) {
//         alert("Please select a time.");
//         return;
//     }
//     document.getElementById(activeField).value = `${selectedDate} ${time}`;
//     document.getElementById("timePickerModal").classList.add("hidden");
// });

//   // Cancel time selection
//   document.getElementById("modalCancel").addEventListener("click", () => {
//   document.getElementById("timePickerModal").classList.add("hidden");
//   });


  // for the room page


