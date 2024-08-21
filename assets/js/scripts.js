const orderHistory = [
    {
        order_id: "1001",
        order_date: "2024-06-01",
        items_purchased: [
            {item_name: "Laptop", quantity: 1, price: 1200.00},
            {item_name: "Mouse", quantity: 1, price: 25.00}
        ],
        total_amount: 1225.00,
        order_status: "Delivered",
        delivery_address: "1234 Elm Street, Springfield, IL, 62704",
        delivery_date: "2024-06-03"
    },
    {
        order_id: "1002",
        order_date: "2024-06-02",
        items_purchased: [
            {item_name: "Smartphone", quantity: 1, price: 799.99},
            {item_name: "Earbuds", quantity: 1, price: 50.00}
        ],
        total_amount: 849.99,
        order_status: "Shipped",
        delivery_address: "5678 Oak Street, Springfield, IL, 62705",
        delivery_date: "2024-06-05"
    }
];

function renderOrderHistory(orders) {
    const tbody = document.getElementById('order-history-body');
    orders.forEach(order => {
        const tr = document.createElement('tr');

        const tdOrderId = document.createElement('td');
        tdOrderId.textContent = order.order_id;
        tr.appendChild(tdOrderId);

        const tdOrderDate = document.createElement('td');
        tdOrderDate.textContent = order.order_date;
        tr.appendChild(tdOrderDate);

        const tdItemsPurchased = document.createElement('td');
        const items = order.items_purchased.map(item => `${item.item_name} (x${item.quantity}) - $${item.price}`).join('<br>');
        tdItemsPurchased.innerHTML = items;
        tr.appendChild(tdItemsPurchased);

        const tdTotalAmount = document.createElement('td');
        tdTotalAmount.textContent = `$${order.total_amount.toFixed(2)}`;
        tr.appendChild(tdTotalAmount);

        const tdOrderStatus = document.createElement('td');
        tdOrderStatus.textContent = order.order_status;
        tr.appendChild(tdOrderStatus);

        const tdDeliveryAddress = document.createElement('td');
        tdDeliveryAddress.textContent = order.delivery_address;
        tr.appendChild(tdDeliveryAddress);

        const tdDeliveryDate = document.createElement('td');
        tdDeliveryDate.textContent = order.delivery_date;
        tr.appendChild(tdDeliveryDate);

        tbody.appendChild(tr);
    });
}

document.addEventListener('DOMContentLoaded', () => {
    renderOrderHistory(orderHistory);
});
