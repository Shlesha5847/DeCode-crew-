
document.addEventListener('DOMContentLoaded', function() {
    // Sample test data
    let tests = [
        {
            id: 1,
            type: 'Mathematics',
            level: 'Class 10th',
            levelAchieved: 'B',
            score: 85,
            date: '2025-03-15',
            status: 'graded'
        },
        {
            id: 2,
            type: 'English',
            level: 'Class 9th',
            levelAchieved: 'A',
            score: 92,
            date: '2025-03-10',
            status: 'graded'
        },
        {
            id: 3,
            type: 'Science',
            level: 'Class 8th',
            levelAchieved: 'C',
            score: 78,
            date: '2025-03-05',
            status: 'graded'
        }
    ];
    
    
    // File upload handling
    const fileUploadArea = document.getElementById('file-upload-area');
    const fileInput = document.getElementById('file-input');
    const fileNameDisplay = document.getElementById('file-name');
    
    fileUploadArea.addEventListener('click', () => {
        fileInput.click();
    });
    
    fileUploadArea.addEventListener('dragover', (e) => {
        e.preventDefault();
        fileUploadArea.style.borderColor = getComputedStyle(document.documentElement).getPropertyValue('--primary-color');
        fileUploadArea.style.backgroundColor = '#f0f2ff';
    });
    
    fileUploadArea.addEventListener('dragleave', () => {
        fileUploadArea.style.borderColor = '#ddd';
        fileUploadArea.style.backgroundColor = 'transparent';
    });
    
    fileUploadArea.addEventListener('drop', (e) => {
        e.preventDefault();
        fileUploadArea.style.borderColor = '#ddd';
        fileUploadArea.style.backgroundColor = 'transparent';
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            fileInput.files = files;
            fileNameDisplay.textContent = `Selected file: ${files[0].name}`;
        }
    });
    
    fileInput.addEventListener('change', () => {
        if (fileInput.files.length > 0) {
            fileNameDisplay.textContent = `Selected file: ${fileInput.files[0].name}`;
        } else {
            fileNameDisplay.textContent = '';
        }
    });
    
    // Form submission handling
    const testForm = document.getElementById('test-form');
    
    testForm.addEventListener('submit', (e) => {
        e.preventDefault();
        
        const testType = document.getElementById('test-type').value;
        const level = document.getElementById('level').value;
        
        // Create a score
        const score = Math.floor(Math.random() * 31) + 70; // 70-100
        
        // Create a new test object
        const newTest = {
            id: tests.length + 1,
            type: document.getElementById('test-type').options[document.getElementById('test-type').selectedIndex].text,
            level: document.getElementById('level').options[document.getElementById('level').selectedIndex].text,
            score: score,
            date: new Date().toISOString().split('T')[0],
            status: 'graded'
        };
        
        // Add to tests array
        tests.push(newTest);
        
        // Update UI
        renderTestList();
        
        // Reset form
        testForm.reset();
        fileNameDisplay.textContent = '';
        
        // Show success message
        alert('Test results submitted successfully!');
    });
    
    // Portal cards interaction
    const portalCards = document.querySelectorAll('.portal-card');
    portalCards.forEach(card => {
        card.addEventListener('mouseenter', () => {
            card.style.transform = 'translateY(-15px) scale(1.05) rotateX(10deg)';
        });
        
        card.addEventListener('mouseleave', () => {
            card.style.transform = 'translateY(0) scale(1) rotateX(0)';
        });
        
        card.addEventListener('click', () => {
            const title = card.querySelector('h2').textContent;
            alert(`${title} will be available soon!`);
        });
    });
    
    
    // Add 3D perspective effect to cards
    const cards = document.querySelectorAll('.card');
    
    cards.forEach(card => {
        card.addEventListener('mousemove', function(e) {
            const rect = this.getBoundingClientRect();
            const x = e.clientX - rect.left;
            const y = e.clientY - rect.top;
            
            const centerX = rect.width / 2;
            const centerY = rect.height / 2;
            
            const angleX = (y - centerY) / 20;
            const angleY = (centerX - x) / 20;
            
            this.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) translateZ(10px)`;
        });
        
        card.addEventListener('mouseleave', function() {
            this.style.transform = 'rotateX(0) rotateY(0) translateZ(0)';
        });
    });
});
