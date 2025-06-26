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
  let activeField = null;
  let selectedDate = "";

  // Setup Flatpickr for Check In
  flatpickr("#checkinInput", {
  dateFormat: "Y-m-d",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      selectedDate = dateStr;
      activeField = "checkinInput";
      document.getElementById("modalTime").value = "";
      document.getElementById("timePickerModal").classList.remove("hidden");
      document.getElementById("modalTitle").textContent = `Select Time for ${dateStr}`;
      }
  }
  });

  // Setup Flatpickr for Check Out
  flatpickr("#checkoutInput", {
  dateFormat: "Y-m-d",
  onChange: function (selectedDates, dateStr) {
      if (dateStr) {
      selectedDate = dateStr;
      activeField = "checkoutInput";
      document.getElementById("modalTime").value = "";
      document.getElementById("timePickerModal").classList.remove("hidden");
      document.getElementById("modalTitle").textContent = `Select Time for ${dateStr}`;
      }
  }
  });

  // Confirm time selection
// Confirm time selection
document.getElementById("modalConfirm").addEventListener("click", () => {
    const time = document.getElementById("modalTime").value;
    if (!time) {
        alert("Please select a time.");
        return;
    }
    document.getElementById(activeField).value = `${selectedDate} ${time}`;
    document.getElementById("timePickerModal").classList.add("hidden");
});

  // Cancel time selection
  document.getElementById("modalCancel").addEventListener("click", () => {
  document.getElementById("timePickerModal").classList.add("hidden");
  });






  // for the room page


