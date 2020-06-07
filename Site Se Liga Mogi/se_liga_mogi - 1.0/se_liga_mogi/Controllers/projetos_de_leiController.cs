using System;
using System.Collections.Generic;
using System.Data;
using System.Data.Entity;
using System.Linq;
using System.Net;
using System.Web;
using System.Web.Mvc;
using PagedList;
using se_liga_mogi.Models;

namespace se_liga_mogi.Controllers
{
    public class projetos_de_leiController : Controller 
    {
        private Se_Liga_MogiEntities1 db = new Se_Liga_MogiEntities1();

        public ActionResult Index(int pagina = 1, 
            string Pesquisa = "", 
            string AnoFiltro = ""
            )
        {
            var q = db.projetos_de_lei.AsQueryable();
            if (!string.IsNullOrEmpty(Pesquisa))
            {

                q = q.Where(c => c.numero_projeto.Contains(Pesquisa));
            }
            q = q.OrderBy(c => c.autor_projeto);

            if (!string.IsNullOrEmpty(AnoFiltro)) {
                //q = q.Where(c => c.ano_projeto = int.Parse(AnoFiltro));
            }       

            int AnoAtual = DateTime.Now.Year;

            AnoAtual = AnoAtual - 2005; 

            List<SelectListItem> Anos = new List<SelectListItem>();

            for (int i = 0; i <= AnoAtual; i++) {
                string valor = (i + 2005).ToString();
                Anos.Add(new SelectListItem() { Text = valor, Value =valor });
            }

            SelectList AnosSelecao = new SelectList(Anos, "Text", "Value");

            ViewBag.Anos = AnosSelecao;
            ViewBag.CurrentSort = Pesquisa;
            return View(q.ToPagedList(pagina, 10));
        }
        public ActionResult Detalhes(int? id)
        {
            if (id == null)
            {
                return new HttpStatusCodeResult(HttpStatusCode.BadRequest);
            }
            projetos_de_lei projetos_de_lei = db.projetos_de_lei.Find(id);
            if (projetos_de_lei == null)
            {
                return HttpNotFound();
            }
            return View(projetos_de_lei);
        }
    }
}
