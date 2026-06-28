// TaskFlow — shared utilities

document.addEventListener('DOMContentLoaded', () => {
  // Mobile nav toggle
  const navToggle = document.getElementById('nav-toggle');
  const mobileMenu = document.getElementById('mobile-menu');
  if (navToggle && mobileMenu) {
    navToggle.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
    });
  }

  // Flash message auto-dismiss
  document.querySelectorAll('.flash').forEach(el => {
    setTimeout(() => el.remove(), 4000);
  });

  // Active nav link highlight
  const currentPath = window.location.pathname;
  document.querySelectorAll('nav a').forEach(link => {
    if (link.getAttribute('href') === currentPath) {
      link.classList.add('active', 'text-effortel-accent');
      link.classList.remove('text-gray-400');
    }
  });

  // Smooth scroll for anchor links
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', e => {
      const target = document.querySelector(anchor.getAttribute('href'));
      if (target) {
        e.preventDefault();
        target.scrollIntoView({ behavior: 'smooth' });
      }
    });
  });

  // Set current date if element exists
  const dateEl = document.getElementById('current-date');
  if (dateEl) {
    const options = { weekday: 'long', month: 'short', day: 'numeric' };
    dateEl.textContent = new Date().toLocaleDateString('en-US', options).toUpperCase();
  }

  // Handle checkboxes
  document.querySelectorAll('.checkbox').forEach(cb => {
    cb.addEventListener('click', (e) => {
      e.currentTarget.classList.toggle('checked');
      // If there's an SVG inside, toggle it or add it
      if (e.currentTarget.classList.contains('checked')) {
        e.currentTarget.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
        const taskText = e.currentTarget.nextElementSibling;
        if(taskText) taskText.classList.add('opacity-50', 'line-through');
      } else {
        e.currentTarget.innerHTML = '';
        const taskText = e.currentTarget.nextElementSibling;
        if(taskText) taskText.classList.remove('opacity-50', 'line-through');
      }
    });
  });

  // Populate mock profile data
  const userNameEl = document.getElementById('user-name');
  if (userNameEl && userNameEl.textContent === 'Loading...') {
    userNameEl.textContent = 'Aditya';
  }

  const displayNameEl = document.getElementById('display-name');
  if (displayNameEl && displayNameEl.textContent === 'Loading...') {
    displayNameEl.textContent = 'Aditya Singh';
  }

  const displayEmailEl = document.getElementById('display-email');
  if (displayEmailEl && displayEmailEl.textContent === '—') {
    displayEmailEl.textContent = 'aditya@example.com';
  }

  const displayJoinedEl = document.getElementById('display-joined');
  if (displayJoinedEl && displayJoinedEl.textContent === '—') {
    displayJoinedEl.textContent = 'Joined Oct 2023';
  }
});

// API helper
async function apiFetch(url, options = {}) {
  const token = localStorage.getItem('token');
  const headers = { 'Content-Type': 'application/json', ...options.headers };
  if (token) headers['Authorization'] = `Bearer ${token}`;
  const res = await fetch(url, { ...options, headers });
  if (res.status === 401) {
    localStorage.removeItem('token');
    window.location.href = '/login';
    return;
  }
  return res;
}

// Global functions for inline onclick handlers
window.logout = function() {
  localStorage.removeItem('token');
  window.location.href = '/login';
};

window.newNote = function() {
  window.location.href = '/notes';
};

window.quickAddTask = function() {
  const input = document.getElementById('quick-task');
  if (!input || !input.value.trim()) return;

  const taskList = document.getElementById('task-list');
  if (taskList) {
    const newTask = document.createElement('div');
    newTask.className = 'task-item bg-black/20 p-4 rounded-xl border border-white/5 hover:border-effortel-accent/30 transition-colors cursor-pointer group flex items-start gap-3';
    newTask.innerHTML = `
      <div class="checkbox"></div>
      <div class="flex-1">
        <div class="text-white font-medium mb-1 group-hover:text-effortel-accent transition-colors">${input.value}</div>
        <div class="flex items-center gap-3">
          <span class="badge-priority badge-medium">MEDIUM</span>
          <span class="text-xs text-gray-500 font-mono">Just now</span>
        </div>
      </div>
    `;

    // Add click event for new checkbox
    const cb = newTask.querySelector('.checkbox');
    cb.addEventListener('click', (e) => {
      e.currentTarget.classList.toggle('checked');
      if (e.currentTarget.classList.contains('checked')) {
        e.currentTarget.innerHTML = `<svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="black" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"></polyline></svg>`;
        newTask.querySelector('.flex-1').classList.add('opacity-50', 'line-through');
      } else {
        e.currentTarget.innerHTML = '';
        newTask.querySelector('.flex-1').classList.remove('opacity-50', 'line-through');
      }
    });

    taskList.prepend(newTask);
    input.value = '';
  }
};

// Handle enter key in quick add
document.addEventListener('keydown', (e) => {
  if (e.key === 'Enter' && document.activeElement.id === 'quick-task') {
    window.quickAddTask();
  }
});

// Profile Actions
window.saveProfile = function() {
  const msg = document.getElementById('profile-msg');
  if (msg) {
    msg.textContent = '[ SYSTEM: Aura gained. Profile updated successfully. ]';
    msg.className = 'success-msg mt-4 block';
    setTimeout(() => { msg.classList.add('hidden'); }, 3000);
  }
};

window.changePassword = function() {
  const msg = document.getElementById('pw-msg');
  if (msg) {
    msg.textContent = '[ SYSTEM: Locked in. Password updated securely. ]';
    msg.className = 'success-msg mt-4 block';
    setTimeout(() => { msg.classList.add('hidden'); }, 3000);
  }
};

window.deleteAccount = function() {
  if(confirm("Are you absolutely sure you want to delete your workspace? This action is irreversible.")) {
    window.logout();
  }
};