export default function Footer() {
  return (
    <footer className="bg-[#050505] pt-16 pb-8 px-6 text-white/50 text-sm border-t border-white/5 relative z-10">
      <div className="max-w-6xl mx-auto">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10 mb-16">
          <div className="flex flex-col gap-4">
            <span className="text-xl font-bold tracking-tight text-white mb-2">Lanskaya.</span>
            <p className="max-w-xs">
              Практический метод перепрошивки реакций и обретения контроля над сценарием своей жизни.
            </p>
          </div>
          
          <div className="flex flex-col gap-4">
            <h4 className="text-white font-medium mb-2">Документы</h4>
            <a href="#" className="hover:text-white transition-colors">Политика конфиденциальности</a>
            <a href="#" className="hover:text-white transition-colors">Договор оферты</a>
            <a href="#" className="hover:text-white transition-colors">Правила оплаты</a>
          </div>

          <div className="flex flex-col gap-4">
            <h4 className="text-white font-medium mb-2">Служба заботы</h4>
            <p>Остались вопросы или не проходит оплата?</p>
            <a href="https://t.me/LanskayaO1esy" target="_blank" rel="noreferrer" className="text-white hover:text-white/80 transition-colors inline-block mt-1">
              Написать в поддержку @LanskayaO1esy
            </a>
          </div>
        </div>
        
        <div className="flex flex-col md:flex-row justify-between items-center pt-8 border-t border-white/10 text-xs">
          <p>© {new Date().getFullYear()} Все права защищены.</p>
          <div className="flex gap-6 mt-4 md:mt-0 text-white/40">
            
            
            
          </div>
        </div>
      </div>
    </footer>
  );
}
