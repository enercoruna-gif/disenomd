'use strict';

const header = document.querySelector('.header');
const menuButton = document.querySelector('.menu-toggle');
const navigation = document.querySelector('#navegacion');
menuButton.hidden = false;
header.classList.add('menu-ready');
menuButton.addEventListener('click', () => {
  const open = menuButton.getAttribute('aria-expanded') !== 'true';
  menuButton.setAttribute('aria-expanded', String(open));
  navigation.classList.toggle('open', open);
});
navigation.addEventListener('click', (event) => {
  if (event.target.closest('a')) {
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
  }
});
header.addEventListener('keydown', (event) => {
  if (event.key === 'Escape' && menuButton.getAttribute('aria-expanded') === 'true') {
    navigation.classList.remove('open');
    menuButton.setAttribute('aria-expanded', 'false');
    menuButton.focus();
  }
});

const list = document.querySelector('#task-list');
const form = document.querySelector('#task-form');
const taskInput = document.querySelector('#task-name');
const createButton = document.querySelector('#new-task');
const announcement = document.querySelector('#panel-status');
let currentView = 'all';

function updateTasks() {
  const tasks = [...list.querySelectorAll('li')];
  const done = tasks.filter((task) => task.querySelector('input').checked).length;
  document.querySelector('#total-count').textContent = tasks.length;
  document.querySelector('#pending-count').textContent = tasks.length - done;
  document.querySelector('#done-count').textContent = done;
  document.querySelector('#progress-count').textContent = `${Math.round(done / tasks.length * 100)} %`;
  let visible = 0;
  for (const task of tasks) {
    const checked = task.querySelector('input').checked;
    const status = task.querySelector('.status');
    status.textContent = checked ? 'Completada' : 'En curso';
    status.className = `status ${checked ? 'done' : 'pending'}`;
    task.hidden = (currentView === 'done' && !checked) || (currentView === 'pending' && checked);
    if (!task.hidden) visible++;
  }
  return { done, total: tasks.length, visible };
}

list.addEventListener('change', (event) => {
  const { done, total } = updateTasks();
  const title = event.target.closest('label').querySelector('span').textContent;
  announcement.textContent = `${title}: ${event.target.checked ? 'completada' : 'en curso'}. ${done} de ${total} tareas completadas. Cambios solo en esta demo.`;
  if (event.target.closest('li').hidden) {
    document.querySelector(`[data-view="${currentView}"]`).focus();
  }
});

document.querySelectorAll('[data-view]').forEach((button) => {
  button.addEventListener('click', () => {
    currentView = button.dataset.view;
    document.querySelectorAll('[data-view]').forEach((item) => {
      const selected = item === button;
      item.classList.toggle('selected', selected);
      item.setAttribute('aria-pressed', String(selected));
    });
    const titles = { all: '¡Buen día, equipo!', pending: 'Tus tareas pendientes', done: 'Trabajo completado' };
    document.querySelector('#view-title').textContent = titles[currentView];
    const { visible } = updateTasks();
    announcement.textContent = visible ? `${visible} tareas en esta vista de ejemplo.` : 'No hay tareas en esta vista. Crea una o cambia de vista.';
  });
});

createButton.hidden = false;
createButton.addEventListener('click', () => {
  form.hidden = false;
  taskInput.focus();
});
document.querySelector('#cancel-task').addEventListener('click', () => {
  form.hidden = true;
  form.reset();
  createButton.focus();
});
form.addEventListener('submit', (event) => {
  event.preventDefault();
  const title = taskInput.value.trim();
  if (!title) {
    taskInput.setCustomValidity('Escribe un nombre para la tarea.');
    taskInput.reportValidity();
    return;
  }
  const item = document.createElement('li');
  const label = document.createElement('label');
  const checkbox = document.createElement('input');
  checkbox.type = 'checkbox';
  const name = document.createElement('span');
  name.textContent = title;
  label.append(checkbox, name);
  const assignee = document.createElement('span');
  assignee.className = 'assignee peach';
  assignee.textContent = 'Tú';
  const status = document.createElement('span');
  status.className = 'status pending';
  status.textContent = 'En curso';
  item.append(label, assignee, status);
  list.append(item);
  if (currentView === 'done') document.querySelector('[data-view="all"]').click();
  updateTasks();
  form.reset();
  form.hidden = true;
  checkbox.focus();
  announcement.textContent = `Tarea de ejemplo añadida: ${title}. No se guarda al recargar.`;
});
taskInput.addEventListener('input', () => taskInput.setCustomValidity(''));

document.querySelectorAll('[name="billing"]').forEach((radio) => {
  radio.addEventListener('change', () => {
    const annual = radio.value === 'annual';
    document.querySelectorAll('[data-month]').forEach((price) => {
      price.textContent = `${annual ? price.dataset.year : price.dataset.month} €`;
    });
    document.querySelector('#billing-note').textContent = annual
      ? 'Vista anual ilustrativa: 96 €, 240 € y 384 € al año. No se realizará ningún cobro.'
      : 'Importes mensuales ilustrativos. No se realizará ningún cobro.';
  });
});
document.querySelectorAll('.choose-plan').forEach((link) => {
  link.addEventListener('click', () => {
    announcement.textContent = `Vista de ejemplo del plan ${link.dataset.plan}. No se ha contratado nada ni creado una cuenta.`;
  });
});
