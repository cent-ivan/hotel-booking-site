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

  // Booking Form Submission with URL Parameters
  // let activeField = null;
  let checkInInput;
  let checkOutInput;

  // Setup Flatpickr for Check In
  flatpickr("#checkinInput", {
  dateFormat: "m-d-Y",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      checkInDate = dateStr;
      }
      
  }
  });

  // Setup Flatpickr for Check Out
  flatpickr("#checkoutInput", {
  dateFormat: "m-d-Y",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      checkOutDate = dateStr;
      // activeField = "checkoutInput";
      // document.getElementById("modalTime").value = "";
      // document.getElementById("timePickerModal").classList.remove("hidden");
      // document.getElementById("modalTitle").textContent = `Select Time for ${dateStr}`;
      }
  }
  });
  let selectedRooms = []  

  const totalNight =  document.getElementById('room-total')
  totalNight.textContent = 0
  let room1 = 0
  let room2 = 0
  let room3 = 0

 const roomDropDown = document.getElementById('select-room-dropdown') 
 roomDropDown.addEventListener('change', function() {
  room1 = this.value
  count = parseInt(room1) + parseInt(room2);
  totalNight.textContent = count
 })

 const roomDropDown2= document.getElementById('select-room-dropdown2') 
 roomDropDown2.addEventListener('change', function() {
  room2 = this.value
  count = parseInt(room1) + parseInt(room2);
  totalNight.textContent = count
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


