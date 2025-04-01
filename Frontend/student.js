

// Simple toggle between login and dashboard for demo purposes
document.getElementById('login-btn').addEventListener('click', function() {
    // document.getElementById('login-page').style.display = 'none';
    // document.getElementById('dashboard-page').style.display = 'block';
    window.location.href='new.html';
});

// Tab switching functionality
document.querySelectorAll('.tab').forEach(tab => {
    tab.addEventListener('click', function() {
        // Remove active class from all tabs
        document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
        
        // Add active class to clicked tab
        this.classList.add('active');
        
        // Here you would normally show/hide content based on the selected tab
        // For demo purposes we're just changing the active state
    });
});
