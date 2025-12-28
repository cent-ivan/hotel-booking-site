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


    const checkinDate = new Date(checkin)
    const checkoutDate = new Date(checkout)
    const totalNights = (checkoutDate - checkinDate) / (1000 * 60 * 60 * 24);
    total.value = totalNights 
    totalMobile.textContent = totalNights
  }


  // Booking Form Submission with URL Parameters
  // let activeField = null;
  const checkInInput = document.getElementById('checkinInput')
  const checkOutInput = document.getElementById('checkoutInput')
  let minCheckoutDate = document.getElementById('checkin-date');

  // Setup Flatpickr for Check In
  flatpickr("#checkinInput", {
  dateFormat: "Y-m-d",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      checkInDate.value = dateStr;
      minCheckoutDate = dateStr;
      }
  }
  });

  // Setup Flatpickr for Check Out
  flatpickr("#checkoutInput", {
  dateFormat: "Y-m-d",
  minDate:`${checkInInput.value}`,
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
  //CASE: resets the price if new

  
  //Room Tracking Code
  const displayRooms = document.getElementById('display-rooms')










  //Add event listeners to all dropdowns
  // const roomDropDowns = document.querySelectorAll('#select-room-dropdown')
  // const roomTypeNames = document.querySelectorAll('#room-name') //get all of the room name
  // const roomPrices = document.querySelectorAll('#room-price')
  
  // let count = 0 //for accessing the room type nodelist. SEE: roomTypeIds 
  // roomDropDowns.forEach(dropdown => {
  //     const roomName =  roomTypeNames[count].outerText //retrieve the text value from the nodelist
  //     const roomPrice = roomPrices[count].outerText
      
  //     dropdown.addEventListener('change', function() {     
  //         rooms[roomName] = {num: this.value, price:roomPrice} //Data selected by the customer. Actual data structure     
            

  //           //CASE: Deleted the old content
  //           if (displayRooms.innerHTML !== '') {
  //             displayRooms.innerHTML = "";
  //           }

  //         totalPrice = 0
          
  //         const price = roomPrice * this.value
  //         for (key in rooms) {
  //           if(rooms[key].num === '0') {
  //             delete rooms[key]
  //             console.log('deleted')
  //           }

  //           //decrease the computed price
  //           if (!(roomName in rooms)) {
  //             totalPrice -= price
  //           } else {
  //             //for display
  //             //assign new value
  //             const newPara = document.createElement('input')
  //             newPara.readOnly = true
  //             newPara.name = `room-${key.replaceAll(' ','')}`
  //             newPara.classList = "text-xs outline-0"
  //             //Outputs the newest data
  //             newPara.value = `${rooms[key].num}x ${key}`
  //             displayRooms.appendChild(newPara)
  //             console.log('added')

  //             const roomPrice =  rooms[key].price * rooms[key].num
  //             totalPrice += roomPrice
  //           }
            
  //         }
  //         //Compute first and update the total

    
  //         priceElem.value = parseFloat(totalPrice)
  //         priceElemMobile.innerText = parseFloat(totalPrice)
  //         console.log(rooms)
          
  //     })

  //     count += 1 //adds for next index
  // })
  
  






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


