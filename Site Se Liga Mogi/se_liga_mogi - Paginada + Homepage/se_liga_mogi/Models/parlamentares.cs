//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated from a template.
//
//     Manual changes to this file may cause unexpected behavior in your application.
//     Manual changes to this file will be overwritten if the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace se_liga_mogi.Models
{
    using System;
    using System.Collections.Generic;
    
    public partial class parlamentares
    {
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2214:DoNotCallOverridableMethodsInConstructors")]
        public parlamentares()
        {
            this.projetos_de_lei = new HashSet<projetos_de_lei>();
        }
    
        public int id_parlamentar { get; set; }
        public string nome_parlamentar { get; set; }
        public string cargo_parlamentar { get; set; }
        public Nullable<int> total_faltas { get; set; }
    
        public virtual presenca_parlamentares presenca_parlamentares { get; set; }
        [System.Diagnostics.CodeAnalysis.SuppressMessage("Microsoft.Usage", "CA2227:CollectionPropertiesShouldBeReadOnly")]
        public virtual ICollection<projetos_de_lei> projetos_de_lei { get; set; }
    }
}