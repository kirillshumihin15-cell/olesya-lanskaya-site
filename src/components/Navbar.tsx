import { useState } from 'react';

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="absolute top-6 left-1/2 -translate-x-1/2 z-50">
      <div className="bg-white rounded-full shadow-lg flex items-center justify-between px-6 py-3 w-[200px]">
        <span className="text-lg font-bold tracking-tight text-black">Lanskaya.</span>
        <button 
          onClick={() => setIsOpen(!isOpen)}
          className="relative w-6 h-6 flex items-center justify-center focus:outline-none"
        >
          <span 
            className={`absolute h-[2px] w-5 bg-black transform transition-transform duration-300 ease-[cubic-bezier(0.77,0,0.175,1)] ${isOpen ? 'rotate-45' : '-translate-y-1'}`}
          />
          <span 
            className={`absolute h-[2px] w-5 bg-black transform transition-transform duration-300 ease-[cubic-bezier(0.77,0,0.175,1)] ${isOpen ? '-rotate-45' : 'translate-y-1'}`}
          />
        </button>
      </div>

      <div 
        className={`absolute top-full left-0 w-full mt-2 bg-white rounded-2xl shadow-lg flex flex-col overflow-hidden transition-all duration-300 transform origin-top ${isOpen ? 'opacity-100 scale-100 translate-y-0 pointer-events-auto' : 'opacity-0 scale-95 -translate-y-2 pointer-events-none'}`}
      >
        <a href="#method" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Метод</a>
        <a href="#about" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Обо мне</a>
        <a href="#reviews" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Отзывы</a>
              <a href="#faq" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">FAQ</a>
              <a href="#inside" className="px-6 py-3 text-black text-sm font-medium hover:bg-gray-50 transition-colors border-b border-gray-100">Формат</a>
      </div>
    </div>
  );
}
