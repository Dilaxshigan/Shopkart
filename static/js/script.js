document.addEventListener("DOMContentLoaded", function() {
  const btnPlus = document.getElementById("btnPlus");
  const btnMinus = document.getElementById("btnMinus");
  const txtQty = document.getElementById("txtQty");
  const pid = document.getElementById("pid");
  const btnCart = document.getElementById("btnCart");

  // ✅ Get CSRF token from meta tag
  const csrftoken = document.querySelector('[name=csrf-token]').content;

  btnPlus.addEventListener("click", function() {
    let qty = parseInt(txtQty.value, 10);
    qty = isNaN(qty) ? 0 : qty;
    if (qty < 10) {
      txtQty.value = qty + 1;
    }
  });

  btnMinus.addEventListener("click", function() {
    let qty = parseInt(txtQty.value, 10);
    qty = isNaN(qty) ? 0 : qty;
    if (qty > 1) {
      txtQty.value = qty - 1;
    }
  });

  btnCart.addEventListener("click", function() {
    let qty = parseInt(txtQty.value, 10);
    qty = isNaN(qty) ? 0 : qty;

    if (qty > 0) {
      const postObj = {
        product_qty: qty,
        pid: pid.value
      };

      fetch("/addtocart", {
        method: 'POST',
        credentials: 'same-origin',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/json',
          'X-Requested-With': 'XMLHttpRequest',
          'X-CSRFToken': csrftoken  // ✅ CSRF token passed here
        },
        body: JSON.stringify(postObj)
      })
      .then(response => response.json())
      .then(data => {
        alert(data.status);
      });

    } else {
      alert("Please Enter The Quantity");
    }
  });
});
